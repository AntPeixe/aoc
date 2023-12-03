use std::collections::HashMap;

fn main() {
    let cubes: HashMap<&str, u8> = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);

    // Part 1
    let data: i32 = include_str!("../input.txt")
        .split('\n')
        .map(|game_line| {
            if game_line.is_empty() {
                return 0;
            }
            let game: Vec<&str> = game_line.split(':').collect();
            let game_id = game[0].split(' ').collect::<Vec<&str>>()[1]
                .parse::<i32>()
                .unwrap();
            for set in game[1].split(';').collect::<Vec<&str>>() {
                let set = set.replace(',', "");
                let set_splits = set.trim().split(' ').collect::<Vec<&str>>();
                let n_revealed = set_splits.len() / 2;
                for i in 0..n_revealed {
                    if set_splits[i * 2].parse::<u8>().unwrap() > cubes[set_splits[i * 2 + 1]] {
                        return 0;
                    }
                }
            }
            return game_id;
        })
        .sum();
    println!("Part 1: {:?}", data);

    // Part 2
    let data: i32 = include_str!("../input.txt")
        .split('\n')
        .map(|game_line| {
            if game_line.is_empty() {
                return 0;
            }
            let game: Vec<&str> = game_line.split(':').collect();
            let mut cubes: HashMap<String, i32> = HashMap::from([
                (String::from("red"), 0),
                (String::from("green"), 0),
                (String::from("blue"), 0),
            ]);
            for set in game[1].split(';').collect::<Vec<&str>>() {
                let set = set.replace(',', "");
                let set_splits = set.trim().split(' ').collect::<Vec<&str>>();
                let n_revealed = set_splits.len() / 2;
                for i in 0..n_revealed {
                    let color = set_splits[i * 2 + 1];
                    let current_count = *cubes.get(color).unwrap();
                    let n = set_splits[i * 2].parse::<u8>().unwrap();
                    cubes.insert(color.to_string(), current_count.max(n as i32));
                }
            }
            return cubes.values().product();
        })
        .sum();
    println!("Part 1: {:?}", data);
}
