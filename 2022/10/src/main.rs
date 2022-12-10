fn main() {
    let important_cycles = vec![20, 60, 100, 140, 180, 220];
    let (_, _, acc) = include_str!("../input.txt")
        .lines()
        .fold((1, 1, 0), |(cycle, x_reg, acc), line| {
            let mut new_acc = acc;

            if important_cycles.contains(&cycle) {
                new_acc = new_acc + (cycle * x_reg);
            }

            if line == "noop" {
                (cycle + 1, x_reg, new_acc)

            } else {
                // check if the skip cycle is one to keep track of
                if important_cycles.contains(&(cycle+1)) {
                    new_acc = new_acc + ((cycle+1) * x_reg);
                }

                let (_, amount) = line.split_once(' ').expect("it must be splitable");
                let amount = amount.parse::<i32>().expect("it must parsable");

                (cycle + 2, x_reg + amount, new_acc)
            }
        });

    println!("{}", acc);
}

