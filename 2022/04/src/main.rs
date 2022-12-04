fn parse_convert(s: &str) -> (i32, i32) {
    let (a, b) = s.split_once('-').expect("aoc mistake");
    (a.parse::<i32>().expect("aoc mistake"), b.parse::<i32>().expect("aoc mistake"))
}


fn main() {
    let contains = include_str!("../input.txt")
        .lines()
        .map(|line| {
            let (one, two) =  line.split_once(',').expect("aoc mistake");
            let (one, two) = (parse_convert(one), parse_convert(two));
            (one.0 <= two.0 && one.1 >= two.1 || two.0 <= one.0 && two.1 >= one.1) as i32
        });

    println!("Part 1: {:?}", contains.sum::<i32>());

    let contains = include_str!("../input.txt")
        .lines()
        .map(|line| {
            let (one, two) =  line.split_once(',').expect("aoc mistake");
            let (one, two) = (parse_convert(one), parse_convert(two));
            (one.0 <= two.0 && one.1 >= two.0 || two.0 <= one.0 && two.1 >= one.0) as i32
        });

    println!("Part 2: {:?}", contains.sum::<i32>());
}
