use std::collections::HashSet;

fn main() {
    // Part 1
    let prio1: u32= include_str!("../input.txt")
        .split('\n')
        .map(|line| {
            let half = line.len() / 2;
            let first = line[..half].as_bytes();
            let second = line[half..].as_bytes();
            let mut prio: u8 = 0;
            for ch in first {
                if second.contains(ch) {
                    if 97 <= *ch && *ch <= 122 { prio = *ch - 96; }
                    else { prio = *ch - 65 + 27; }
                    break;
                }
            }
            prio as u32
        })
        .sum();
    println!("{:?}", prio1);

    // Part 2
    let lines: Vec<&str> = include_str!("../input.txt").lines().collect();
    let mut prios2: Vec<u32> = Vec::new();
    for idx in (0..lines.len()).step_by(3) {
        let one: HashSet<&u8> = lines[idx].as_bytes().into_iter().collect();
        let two: HashSet<&u8> = lines[idx+1].as_bytes().into_iter().collect();
        let three: HashSet<&u8> = lines[idx+2].as_bytes().into_iter().collect();

        let common: Vec<&u8> = one.into_iter().filter(|x| two.contains(x)).filter(|x| three.contains(x)).collect();
        let mut prio: u8 = 0;
        if let Some(&&x) = common.get(0) {
            if 97 <= x && x <= 122 { prio = x - 96; }
            else { prio = x - 65 + 27; }
        }

        prios2.push(prio as u32);
    }
        
    println!("{:?}", prios2.into_iter().sum::<u32>());
}
