//! Deliberately synthetic alternatives, NOT Digicomp DR-70 output.
use std::env;

const CIRCLE: u32 = 36_000;
const SIGN: u32 = 3_000;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Model { Equal, WholeSign }

impl Model {
    fn parse(value: &str) -> Result<Self, String> {
        match value {
            "equal" => Ok(Self::Equal),
            "whole-sign" => Ok(Self::WholeSign),
            _ => Err("model must be 'equal' or 'whole-sign'".into()),
        }
    }
    fn name(self) -> &'static str {
        match self { Self::Equal => "equal", Self::WholeSign => "whole-sign" }
    }
}

fn parse_angle(text: &str) -> Result<u32, String> {
    let (degrees, fraction) = text.split_once('.').unwrap_or((text, ""));
    if degrees.is_empty() || !degrees.bytes().all(|b| b.is_ascii_digit()) ||
       fraction.len() > 2 || !fraction.bytes().all(|b| b.is_ascii_digit()) {
        return Err("angle must be decimal degrees with at most 2 decimals".into());
    }
    let whole: u32 = degrees.parse().map_err(|_| "angle out of range")?;
    let dec = if fraction.is_empty() { 0 } else {
        fraction.parse::<u32>().map_err(|_| "bad fraction")? * if fraction.len() == 1 { 10 } else { 1 }
    };
    let value = whole.checked_mul(100).and_then(|n| n.checked_add(dec))
        .ok_or("angle out of range")?;
    if value >= CIRCLE { return Err("angle must be in [0, 360)".into()); }
    Ok(value)
}

fn candidate_houses(ascendant: u32, model: Model) -> [u32; 12] {
    let anchor = match model {
        Model::Equal => ascendant,
        Model::WholeSign => (ascendant / SIGN) * SIGN,
    };
    std::array::from_fn(|i| (anchor + SIGN * i as u32) % CIRCLE)
}

fn render(ascendant: u32, model: Model) -> String {
    let mut out = format!("SYNTHETIC DR70 CANDIDATE | model={} | input_asc={:03}.{:02}\n",
        model.name(), ascendant / 100, ascendant % 100);
    for (i, angle) in candidate_houses(ascendant, model).iter().enumerate() {
        out.push_str(&format!("H{:02} {:03}.{:02}\n", i + 1, angle / 100, angle % 100));
    }
    out
}

fn run(args: &[String]) -> Result<String, String> {
    if args.len() != 5 || args[1] != "--ascendant" || args[3] != "--model" {
        return Err("usage: dr70-output-candidates --ascendant 15.25 --model equal|whole-sign".into());
    }
    let angle = parse_angle(&args[2])?;
    let model = Model::parse(&args[4])?;
    Ok(render(angle, model))
}

fn main() {
    let args: Vec<String> = env::args().collect();
    match run(&args) {
        Ok(s) => print!("{s}"),
        Err(e) => { eprintln!("{e}"); std::process::exit(2); }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn parses_exact_centidegrees() {
        assert_eq!(parse_angle("15.2"), Ok(1520));
        assert_eq!(parse_angle("359.99"), Ok(35999));
        for bad in ["360", "-1", "NaN", "15.123", "", "15x", "999999999999"] {
            assert!(parse_angle(bad).is_err(), "{bad}");
        }
    }
    #[test]
    fn same_input_distinguishes_candidates() {
        let equal = candidate_houses(1525, Model::Equal);
        let sign = candidate_houses(1525, Model::WholeSign);
        assert_eq!(equal[0], 1525);
        assert_eq!(sign[0], 0);
        assert_ne!(equal, sign);
        assert_eq!(equal[11], 34525);
    }
    #[test]
    fn some_inputs_are_indistinguishable() {
        assert_eq!(candidate_houses(3000, Model::Equal), candidate_houses(3000, Model::WholeSign));
    }
    #[test]
    fn output_is_labeled_and_has_twelve_fields() {
        let s = render(1525, Model::Equal);
        assert!(s.starts_with("SYNTHETIC DR70 CANDIDATE"));
        assert_eq!(s.lines().count(), 13);
        assert!(s.contains("H01 015.25"));
        assert!(s.contains("H12 345.25"));
        assert!(!s.contains("KOCH"));
    }
}
