fn get_adjacent_idx(idx: usize, line_len: usize, total_len: usize) -> impl Iterator<Item = usize> {
    let line = idx / line_len;
    let total_lines = total_len / line_len;
    let col = idx % line_len;

    return [
        if col != 0 && line != 0 { Some(idx - line_len - 1) } else { None },
        if line != 0 { Some(idx - line_len) } else { None },
        if col != line_len - 1 && line != 0 { Some(idx - line_len + 1) } else { None },
        if col != 0 { Some(idx - 1) } else { None }, if col != line_len - 1 { Some(idx + 1) } else { None },
        if col != 0 && line != total_lines - 1 { Some(idx + line_len - 1) } else { None },
        if line != total_lines - 1 { Some(idx + line_len) } else { None },
        if col != line_len - 1 && line != total_lines - 1 { Some(idx + line_len + 1) } else { None },
    ].into_iter()
        .filter_map(|e| e)
        .into_iter();
}

fn visit_adjacents(
    idx: usize,
    line_len: usize,
    total_len: usize,
    chars: &Vec<char>,
    adjacency: &mut Vec<bool>,
) {
    if adjacency[idx] || chars[idx] == '.' {
        return;
    }
    if chars[idx].is_digit(10) { adjacency[idx] = true; }
    get_adjacent_idx(idx, line_len, total_len)
        .map(|adjacent| visit_adjacents(adjacent, line_len, total_len, chars, adjacency))
        .for_each(drop);
}


fn main() {
    let data = include_str!("../input.txt")
        .split('\n')
        .filter(|s| !s.is_empty())
        .collect::<Vec<&str>>();

    let line_len = data[0].len();

    let data = data.join("");
    let total_len = data.len();

    let chars: Vec<char> = data.chars().collect();

    let mut adjacency: Vec<bool> = vec![false; total_len];
    data.chars()
        .enumerate()
        .filter_map(|(i, c)| match c.is_ascii_punctuation() && c != '.' {
            true => Some(i),
            false => None,
        })
        .map(|symbol_idx| {
            get_adjacent_idx(symbol_idx, line_len, total_len)
                .map(|adjacent| {
                    visit_adjacents(adjacent, line_len, total_len, &chars, &mut adjacency)
                })
                .for_each(drop);
        })
        .for_each(drop);

    let (part1, _) = adjacency.iter()
        .zip(chars.iter())
        .fold((0, 0), |(total, value), (a, c)| {
            if c.is_digit(10) && *a {
                // this works under the assumption that two consecutive lines don't end and start
                // with a number. this would break since it's checking continuous digits and it's
                // using the a 1D array
                // test and my input allows this
                (total, value * 10 + c.to_digit(10).unwrap())
            } else {
                if value != 0 {
                    (total + value, 0)
                } else {
                    (total, value)
                }
            }
        });

    println!("{:?}", part1);


    // Part 2

    let part2: u32 = data.chars()
        .enumerate()
        .filter_map(|(i, c)| match c.is_ascii_punctuation() && c != '.' {
            true => Some(i),
            false => None,
        })
        .map(|symbol_idx| {
            let mut adjacency: Vec<bool> = vec![false; total_len];
            get_adjacent_idx(symbol_idx, line_len, total_len)
                .map(|adjacent| {
                    visit_adjacents(adjacent, line_len, total_len, &chars, &mut adjacency)
                })
                .for_each(drop);
            let mut vec_acc: Vec<u32> = vec![];
            let (parts, _) = adjacency.iter()
                .zip(chars.iter())
                .fold((&mut vec_acc, 0), |(acc_vec, value), (a, c)| {
                    if c.is_digit(10) && *a {
                        // this works under the assumption that two consecutive lines don't end and start
                        // with a number. this would break since it's checking continuous digits and it's
                        // using the a 1D array
                        // test and my input allows this
                        (acc_vec, value * 10 + c.to_digit(10).unwrap())
                    } else {
                        if value != 0 {
                            acc_vec.push(value);
                            (acc_vec, 0)
                        } else {
                            (acc_vec, value)
                        }
                    }
                });
            if parts.len() == 2 {
                return parts.into_iter().fold(1, |acc, e| acc * e.clone());
            }
            else {
                return 0;
            }
        })
        .sum();

    println!("{:?}", part2);
}

