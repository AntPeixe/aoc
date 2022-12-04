use std::collections::HashMap;

fn main() {
    let winnings: HashMap<&str, &str> = HashMap::from([("rock","scissors"), ("scissors","paper"), ("paper","rock")]);
    let plays: HashMap<&str, &str> = HashMap::from([
        ("C","scissors"),
        ("B","paper"),
        ("A","rock"),
        ("Z","scissors"),
        ("Y","paper"),
        ("X","rock"),
    ]);
    let points: HashMap<&str, u32> = HashMap::from([("rock", 1), ("paper", 2), ("scissors", 3)]);

    // Part 1
    // let score: u32 = include_str!("../input.txt")
    //     .split('\n')
    //     .map(|game| {
    //         if game.is_empty() { 0 }
    //         else {
    //             let elf = plays[&game[..1]];
    //             let you = plays[&game[2..]];
    //
    //             if winnings[you] == elf {
    //                 points[you] + 6
    //             } else if winnings[elf] == you {
    //                 points[you]
    //             } else {
    //                 points[you] + 3
    //             }
    //         }
    //     })
    //     .sum();
    // println!("{:?}", score);

    // Part 2
    let lossing: HashMap<&str, &str> = HashMap::from([("scissors","rock"), ("paper","scissors"), ("rock","paper")]);
    let score: u32 = include_str!("../input.txt")
        .split('\n')
        .map(|game| {
            if game.is_empty() { 0 }
            else {
                let elf = plays[&game[..1]];
                let you = &game[2..];

                if you == "X" {  // should loose
                    points[winnings[elf]]
                } else if you == "Z" {  // should win
                    points[lossing[elf]] + 6
                } else {
                    points[elf] + 3
                }
            }
        })
        .sum();
    println!("{:?}", score);
}
