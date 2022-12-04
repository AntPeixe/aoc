fn main() {
    let mut data = include_str!("../input.txt")
        .split("\n\n")
        .map(|n|
             n.split('\n')
             .flat_map(str::parse::<usize>)
             .sum::<usize>()
        )
        .collect::<Vec<usize>>();

    data.sort_by(|a,b| b.cmp(a));
    println!("{:?}", data.into_iter().take(3).sum::<usize>());
}
