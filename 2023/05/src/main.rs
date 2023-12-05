fn main() {
    let mut data = include_str!("../input.txt").split("\n\n");
    let seeds: Vec<u64> = data.next().unwrap().split(':').collect::<Vec<&str>>()[1]
        .trim()
        .split(' ')
        .map(|e| e.parse::<u64>().unwrap())
        .collect();

    let part1 = data
        .fold(seeds, |positions, mapping| {
            // fold over the blocks of mappings
            // keep track of the next "positions" of each seed
            let mut next_positions = vec![];
            mapping.lines()
                .skip(1)
                .map(|map_line| {
                    // for each mapping line check whether a seed would be mapped and make the move
                    let ranges: Vec<u64> = map_line.split(' ').map(|e| e.parse::<u64>().unwrap()).collect();
                    for p in positions.iter() {
                        if *p >= ranges[1] && *p <= ranges[1] + ranges[2] - 1 {
                            next_positions.push(ranges[0] + *p - ranges[1]);
                        }
                    }
                })
                .for_each(drop); // exhaust the iterator
            next_positions
        })
        .into_iter()
        .min()
        .unwrap();
    println!("{:?}", part1);

    let mut data = include_str!("../input.txt").split("\n\n");
    let seeds: Vec<Vec<u64>> = data.next().unwrap().split(':').collect::<Vec<&str>>()[1]
        .trim()
        .split(' ')
        .map(|e| e.parse::<u64>().unwrap())
        .collect::<Vec<u64>>()
        .chunks(2)
        .map(|c| c.to_vec())
        .collect();

    let part2 = data
        .fold(seeds, |positions, mapping| {
            // folding over the blocks of mappings
            // keep track of the unused positions (ranges) and the next positions (mapped)
            let mut unused_positions: Vec<Vec<u64>> = positions.clone();
            let mut next_positions: Vec<Vec<u64>> = vec![];
            mapping.lines()
                .skip(1)
                .map(|map_line| {
                    let ranges: Vec<u64> = map_line.split(' ').map(|e| e.parse::<u64>().unwrap()).collect();
                    let range_end = ranges[1] + ranges[2] - 1;

                    // tmp vars to keep track of next and unsused positions for the present ranges
                    let mut tmp_unused_pos: Vec<Vec<u64>> = vec![];
                    let mut tmp_next_pos: Vec<Vec<u64>> = vec![];

                    // iterate over the available unused positions and fold building the new unused
                    // positions and the next positions for the present range
                    let (next, unused) = unused_positions.iter()
                        .fold((&mut tmp_next_pos, &mut tmp_unused_pos), |(next_pos, not_used), pos_range| {
                            let (start, n) = (pos_range[0], pos_range[1]);
                            if start > range_end || start + n - 1 < ranges[1] {  // outside of current range
                                not_used.push(vec![start, n]);
                            }
                            else if start >= ranges[1] {  // starts inside
                                if start + n - 1 <= range_end {  // fully inside
                                    next_pos.push(vec![ranges[0] + start - ranges[1], n]);
                                } else {  // ends after
                                    next_pos.push(vec![ranges[0] + start - ranges[1], range_end - start + 1]);
                                    not_used.push(vec![range_end + 1, start + n - range_end]);
                                }
                            } else {  // start before
                                if start + n - 1 <= range_end {  // ends inside
                                    next_pos.push(vec![ranges[0], start + n - ranges[1]]);
                                    not_used.push(vec![start, ranges[1] - start]);
                                } else {  // ends after
                                    next_pos.push(vec![ranges[0], ranges[2]]);
                                    not_used.push(vec![start, ranges[1] - start]);
                                    not_used.push(vec![range_end + 1, start + n - range_end]);
                                }
                            }
                            (next_pos, not_used)
                        });
                    // concat the new next positions and replace the available unused ones
                    next_positions = [next_positions.to_owned(), next.to_owned()].concat();
                    unused_positions = unused.to_owned();
                })
                .for_each(drop); // exhaust the iterator
            // for the next block of mappings the positions are all the next positions and any
            // unused ones
            [next_positions, unused_positions].concat()
        })
        .into_iter()
        .map(|chunk| chunk[0])
        .min()
        .unwrap();
    println!("{:?}", part2);
}

