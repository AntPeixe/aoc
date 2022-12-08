// this solution isn't originally mine. Saw the idea in ThePrimeagen stream
// I saw the idea of using a stack to represent the DFS and then implemented it
fn main() {

    let mut stack = vec![0];
    let mut total = 0;

    let lines = include_str!("../input.txt").lines();
    for line in lines {
        if line == "$ ls" || line == "$ cd /" || line.starts_with("dir ") {}
        else if line == "$ cd .." {
            let dir_size = stack.pop().expect("it must exist");
            if dir_size < 100000 { total += dir_size; }
            let previous = stack.pop().expect("it must exist");
            stack.push(previous + dir_size);
        } else if line.starts_with("$ cd ") {
            stack.push(0);
        } else {
            let (size, _) = line.split_once(' ').expect("it must exist");
            let current = stack.pop().expect("it must exist");
            stack.push(current + size.parse::<i32>().expect("it must exist"));
        }
    }

    println!("{:?}", total);
}

