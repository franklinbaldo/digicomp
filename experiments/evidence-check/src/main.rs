//! Compare candidate text against documented fragments.
//! A lexical match is NOT DR-70 fidelity and never authenticates a source.
use std::{env, fs};

#[derive(Debug, PartialEq, Eq)]
enum Verdict { Present, Missing, Inconclusive }
#[derive(Debug)]
struct Fragment<'a> { id: &'a str, family: &'a str, kind: &'a str, token: &'a str }

fn read_fragments(text: &str) -> Result<Vec<Fragment<'_>>, String> {
    let mut out = Vec::new();
    for (line_number, line) in text.lines().enumerate() {
        if line.is_empty() || line.starts_with('#') { continue; }
        let fields: Vec<&str> = line.split('\t').collect();
        if fields.len() != 4 || fields.iter().any(|field| field.is_empty()) {
            return Err(format!("invalid TSV line {}", line_number + 1));
        }
        if !matches!(fields[2], "literal" | "candidate" | "lead") {
            return Err(format!("unknown evidence kind on line {}", line_number + 1));
        }
        out.push(Fragment { id: fields[0], family: fields[1], kind: fields[2], token: fields[3] });
    }
    Ok(out)
}

fn evaluate(fragment: &Fragment<'_>, output: Option<&str>) -> Verdict {
    // A reported field or source lead cannot become a compatibility test
    // merely because the predicted output contains similar text.
    if fragment.kind != "literal" || output.is_none() {
        return Verdict::Inconclusive;
    }
    let value = output.unwrap();
    if value.lines().any(|line| line == fragment.token) {
        Verdict::Present
    } else {
        Verdict::Missing
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        eprintln!("usage: dr70-evidence-check FRAGMENTS.tsv PREDICTED.txt");
        std::process::exit(2);
    }
    let source = fs::read_to_string(&args[1]).expect("cannot read catalog TSV");
    let prediction = fs::read_to_string(&args[2]).expect("cannot read predicted output");
    let evidence = read_fragments(&source).expect("invalid evidence catalog");
    for fragment in evidence {
        let status = evaluate(&fragment, Some(&prediction));
        println!("{}\t{}\t{:?}\t{}", fragment.id, fragment.family, status, fragment.token);
    }
    println!("These are lexical diagnostics, NOT an assessment of DR-70 fidelity.");
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn unknown_origin_cannot_become_a_pass() {
        let f = Fragment{id:"CARLSON",family:"CARLSON-FIG1",kind:"candidate",token:"H01"};
        assert_eq!(evaluate(&f, Some("H01")), Verdict::Inconclusive);
    }
    #[test]
    fn references_without_output_remain_inconclusive() {
        let f = Fragment{id:"NOLLE",family:"NOLLE",kind:"lead",token:"DR-70"};
        assert_eq!(evaluate(&f, Some("DR-70")), Verdict::Inconclusive);
    }
    #[test]
    fn full_literal_lines_are_compared_exactly() {
        let f = Fragment{id:"FAKE",family:"FAKE",kind:"literal",token:"H01 015.25"};
        assert_eq!(evaluate(&f, Some("H01 015.25\n")), Verdict::Present);
        assert_eq!(evaluate(&f, Some("H01 015.250\n")), Verdict::Missing);
        assert_eq!(evaluate(&f, None), Verdict::Inconclusive);
    }
    #[test]
    fn field_ids_alone_do_not_certify_numbers() {
        let sample = "CARLSON\tCARLSON-FIG1\tcandidate\tH01\n";
        let data = read_fragments(sample).unwrap();
        assert_eq!(evaluate(&data[0], Some("H01 000.00")), Verdict::Inconclusive);
    }
    #[test]
    fn parser_rejects_malformed_or_unknown_input() {
        assert!(read_fragments("x\ty\tbogus\tz").is_err());
        assert!(read_fragments("x\ty\tz").is_err());
        assert_eq!(read_fragments("# metadata\n").unwrap().len(), 0);
    }
}
