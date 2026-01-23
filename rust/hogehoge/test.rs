use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let n: usize = stdin.lock().lines().next().unwrap().unwrap().parse().unwrap();

    let mut dp = vec![1; n + 1];

    for i in 2..dp.len() {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    println!("{}", dp[n]);
}