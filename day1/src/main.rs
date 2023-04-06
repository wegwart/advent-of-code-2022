use std::fs;

fn main() {
    let mut file_path = "day1_test.txt".to_string();
    println!("{}", file_path);
    let result = do_work(&file_path, true, false);
    assert!(result == 24000);
    let result_part2 = do_work(&file_path, true, true);
    assert!(result_part2 == 45000);

    file_path = "day1_puzzle.txt".to_string();
    println!("{}", file_path);
    let result = do_work(&file_path, false, false);
    println!("{}", result);
    let result_part2 = do_work(&file_path, false, true);
    println!("{}", result_part2);
}

fn do_work(file_path: &str, print: bool, is_part2: bool) -> i32 {
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let lines = contents.lines();

    let mut sum = 0;
    let mut results = Vec::new();
    for line in lines {
        match line.parse::<i32>() {
            Ok(value) => sum += value,
            Err(_) => {
                results.push(sum);
                sum = 0;
            }
        }
    }
    results.push(sum);
    results.sort();
    results.reverse();
    if print {
        println!("{:?}", results);
    }
    if is_part2 {
        results[0] + results[1] + results[2]
    } else {
        results[0]
    }
}
