//! Documentary layout probe, NOT an emulator or DR-70 output.
 //! Preserves uncertain two-digit groups from one published Carlson figure.
use std::fmt::Write as _;

const DOCUMENTED_PAIRS: &str = include_str!("../../published-pairs.tsv");

#[derive(Debug, PartialEq, Eq)]
struct PublishedPair {
    left: String,
    right: String,
    left_groups: [String; 2],
    right_groups: [String; 2],
}

fn parse_pairs(input: &str) -> Result<Vec<PublishedPair>, String> {
    let mut pairs = Vec::new();
    for (line_no, raw) in input.lines().enumerate() {
        let line = raw.trim_end_matches('\r');
        if line.is_empty() || line.starts_with('#') {
            continue;
        }
        let f: Vec<&str> = line.split('\t').collect();
        if f.len() != 6 {
            return Err(format!("line {}: expected six TSV columns", line_no + 1));
        }
        let pair_number = pairs.len() + 1;
        let left = format!("H{:02}", pair_number);
        let right = format!("H{:02}", pair_number + 6);
        if f[0] != left || f[1] != right {
            return Err(format!("line {}: unexpected house pair/order", line_no + 1));
        }
        if f[2..].iter().any(|s| s.len() != 2 || !s.bytes().all(|b| b.is_ascii_digit())) {
            return Err(format!("line {}: candidate group must contain two digits", line_no + 1));
        }
        pairs.push(PublishedPair {
            left,
            right,
            left_groups: [f[2].into(), f[3].into()],
            right_groups: [f[4].into(), f[5].into()],
        });
    }
    if pairs.len() != 6 {
        return Err(format!("expected six published pairs, found {}", pairs.len()));
    }
    Ok(pairs)
}

fn render(pairs: &[PublishedPair]) -> String {
    let apparent_matches = pairs.iter()
        .filter(|p| p.left_groups == p.right_groups).count();
    let mut out = String::from(
        "RENDERED_PROTOTYPE_NOT_DEVICE_OUTPUT\n\
source=CARLSON-FIG1-1983-1985\n\
status=SECONDARY_VISUAL_CANDIDATE\n\
notation=[GLYPH_UNREAD] is a placeholder, not a source glyph\n",
    );
    for p in pairs {
        let match_label = if p.left_groups == p.right_groups {
            "APPARENT_MATCH"
        } else {
            "APPARENT_DIFFERENCE"
        };
        writeln!(
            out, "{} {} [GLYPH_UNREAD] {} | {} {} [GLYPH_UNREAD] {} | {}",
            p.left, p.left_groups[0], p.left_groups[1],
            p.right, p.right_groups[0], p.right_groups[1], match_label
        ).expect("writing to String");
    }
    writeln!(out, "candidate_pairs={}", pairs.len()).expect("writing to String");
    writeln!(out, "apparent_matches={}", apparent_matches).expect("writing to String");
    writeln!(out, "apparent_differences={}", pairs.len() - apparent_matches).expect("writing to String");
    out.push_str("complete_published_angles=0\nindependent_holdout=0\n\
device_fidelity=NOT_RUN_NO_GOLDEN\n");
    out
}

fn main() {
    match parse_pairs(DOCUMENTED_PAIRS) {
        Ok(pairs) => print!("{}", render(&pairs)),
        Err(error) => {
            eprintln!("invalid secondary documentary transcription: {error}");
            std::process::exit(2);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    const BASELINE: &str = include_str!("../../published-layout-baseline.txt");

    #[test]
    fn documented_carlson_candidate_produces_frozen_baseline() {
        let parsed = parse_pairs(DOCUMENTED_PAIRS).unwrap();
        assert_eq!(parsed.len(), 6);
        assert_eq!(render(&parsed), BASELINE);
        assert!(render(&parsed).contains("complete_published_angles=0"));
        assert!(render(&parsed).contains("device_fidelity=NOT_RUN_NO_GOLDEN"));
    }

    #[test]
    fn changed_pair_is_reported_not_silently_repaired() {
        let altered = DOCUMENTED_PAIRS.replace(
            "H04\tH10\t25\t08\t25\t08",
            "H04\tH10\t25\t08\t26\t08",
        );
        assert_ne!(altered, DOCUMENTED_PAIRS);
        let report = render(&parse_pairs(&altered).unwrap());
        assert!(report.contains("H04 25 [GLYPH_UNREAD] 08 | H10 26 [GLYPH_UNREAD] 08 | APPARENT_DIFFERENCE"));
        assert!(report.contains("apparent_matches=5"));
        assert!(report.contains("apparent_differences=1"));
        assert!(report.contains("device_fidelity=NOT_RUN_NO_GOLDEN"));
    }

    #[test]
    fn refuses_missing_pair_and_unreadable_or_malformed_group() {
        let lines: Vec<&str> = DOCUMENTED_PAIRS.lines().collect();
        let incomplete = lines.iter().filter(|line| !line.starts_with("H06\t")).copied().collect::<Vec<_>>().join("\n");
        assert!(parse_pairs(&incomplete).is_err());
        assert!(parse_pairs(&DOCUMENTED_PAIRS.replace("H01\tH07\t09", "H01\tH07\t??")).is_err());
        assert!(parse_pairs(&DOCUMENTED_PAIRS.replace("H02\tH08", "H02\tH09")).is_err());
        assert!(parse_pairs(&DOCUMENTED_PAIRS.replace("H03\tH09\t09", "H03\tH09\t009")).is_err());
    }
}
