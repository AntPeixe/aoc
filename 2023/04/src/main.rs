fn main() {
    let n_winnings = include_str!("../input.txt")
        .trim()
        .split('\n')
        .filter(|l| !l.is_empty())
        .map(|l| {
            let numbers = l.split(':').collect::<Vec<&str>>()[1].trim();
            let numbers: Vec<_> = numbers.split('|')
                .map(|p| p.trim().split(' ').filter(|n| !n.is_empty()).collect::<Vec<&str>>())
                .collect();
            numbers[1].to_owned().into_iter().filter(|n| numbers[0].contains(n)).count()
        })
        .collect::<Vec<usize>>();

    let part1: u32 = n_winnings.iter().map(|w| if *w == 0 { 0 } else { (2 as u32).pow((w - 1) as u32) }).sum();
    println!("Part1: {:?}", part1);

    let cards_len = n_winnings.len();
    let (part2, _) = n_winnings.into_iter()
        .fold((0 as u32, vec![1 as u32; cards_len]), |(total, copies), n_wins| {
            // accumulator:
            //      1. total number of cards so far
            //      2. extra copies for each of the following cards including the present
            // element the number of matching numbers in the current card
            let copies_current = *copies.first().unwrap();

            // we don't necessarily need to add to the whole iterator, the tail must be chained back
            let tail: Vec<_> = copies.iter().skip(1 + n_wins).cloned().collect();
            let copies = copies.into_iter()
                .skip(1)
                .take(n_wins as usize)
                .map(|e| e + copies_current)
                .chain(tail)
                .collect();
            (total + copies_current, copies)
        });
    println!("Part2: {:?}", part2);
}

