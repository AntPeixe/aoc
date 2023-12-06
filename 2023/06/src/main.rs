fn main() {
    let data: Vec<Vec<u32>> = include_str!("../input.txt")
        .lines()
        .map(|l| {
            l.split(':').collect::<Vec<&str>>()[1]
                .trim()
                .split_whitespace()
                .map(|e| e.parse::<u32>().unwrap())
                .collect()
        })
        .collect();
    let times = data[0].clone();
    let records = data[1].clone();
    let part1 = times
        .into_iter()
        .zip(records.into_iter())
        .map(|(t, r)| (1..t).map(|n| n * (t - n) > r).filter(|e| *e).count())
        .product::<usize>();
    println!("{:?}", part1);

    let data: Vec<u64> = include_str!("../input.txt")
        .lines()
        .map(|l| {
            l.split(':').collect::<Vec<&str>>()[1]
                .trim()
                .replace(" ", "")
                .parse::<u64>()
                .unwrap()
        })
        .collect();
    let time = data[0];
    let record = data[1];

    let part2 = (1..time)
        .map(|n| n * (time - n) > record)
        .filter(|e| *e)
        .count();
    println!("{:?}", part2);
}
