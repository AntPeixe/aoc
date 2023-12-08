use num::integer::lcm;
use std::collections::HashMap;

fn calculate_steps(
    nodes: &HashMap<String, [String; 2]>,
    moves: &Vec<usize>,
    start: &str,
    condition: impl Fn(&str) -> bool,
) -> usize {
    let mut value = 0;
    let avail_moves = moves.len();
    let mut curr_pos = start;
    loop {
        curr_pos = nodes.get(curr_pos).unwrap()[moves[value % avail_moves]].as_str();
        value = value + 1;
        if condition(curr_pos) {
            break;
        }
    }
    return value;
}

fn main() {
    let mut data = include_str!("../input.txt")
        .lines()
        .filter(|l| !l.is_empty());
    let moves: Vec<usize> = data
        .next()
        .unwrap()
        .chars()
        .map(|c| if c == 'L' { 0 } else { 1 })
        .collect();

    let mut nodes: HashMap<String, [String; 2]> = HashMap::new();
    data.into_iter()
        .map(|l| {
            let l = l.replace(" ", "").replace("(", "").replace(")", "");
            let splits: Vec<&str> = l.split('=').collect();
            let options: Vec<&str> = splits[1].split(',').collect();
            let node = splits[0].to_owned();
            let left = options[0].to_owned();
            let right = options[1].to_owned();
            nodes.insert(node, [left, right]);
        })
        .for_each(drop);

    let part1_condition = |x: &str| x == "ZZZ";
    let part1 = calculate_steps(&nodes, &moves, "AAA", part1_condition);
    println!("part1: {:?}", part1);

    // part 2
    let start_nodes: Vec<_> = nodes.keys().filter(|k| k.ends_with('A')).collect();
    let part2_condition = |x: &str| x.ends_with("Z");
    let part2 = start_nodes
        .into_iter()
        .map(|curr| {
            return calculate_steps(&nodes, &moves, curr, part2_condition);
        })
        .fold(1, |acc, e| lcm(acc, e));
    println!("part2: {:?}", part2);
}

