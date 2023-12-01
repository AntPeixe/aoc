const NUMBERS_WORDS: [&str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
const NUMBERS: [char; 9] = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

fn check_substring(subs: &str, reversed: bool) -> u32 {
    let c = subs.chars().nth(0).unwrap();
    if c.is_digit(10) {
        return c.to_digit(10).unwrap();
    }
    for (ni, n) in NUMBERS_WORDS.iter().enumerate() {
        let num_string = if reversed {n.chars().rev().collect::<String>()} else {n.to_string()};
        if subs.starts_with(num_string.as_str()) {
            return NUMBERS[ni].to_digit(10).unwrap();
        }
    }
    return 0;
}

fn main() {
    // Part 1
    let part1 = include_str!("../input.txt")
        .split('\n')
        .map(|s| {
            let first = s.chars().into_iter().find(|x| x.is_digit(10));
            let last = s.chars().into_iter().rev().find(|x| x.is_digit(10));
            match (first, last) {
                (Some(f), Some(l)) => f.to_digit(10).unwrap() * 10 + l.to_digit(10).unwrap(),
                _ => 0,
            }
        })
        .sum::<u32>();
    println!("Part 1: {:?}", part1);

    // Part 2
    let part2 = include_str!("../input.txt")
        .split('\n')
        .map(|s| {
            let mut first: u32 = 0;
            for i in 0..s.len() {
                let subs = &s[i..];
                let maybe_num = check_substring(subs, false);
                if maybe_num != 0 {
                    first = maybe_num;
                    break;
                }
            }

            let reversed: String = s.chars().rev().collect();
            let mut last: u32 = 0;
            for i in 0..reversed.len() {
                let subs = &reversed[i..];
                let maybe_num = check_substring(subs, true);
                if maybe_num != 0 {
                    last = maybe_num;
                    break;
                }
            }

            first * 10 + last
        })
        .sum::<u32>();
    println!("Part 2: {:?}", part2);
}
