use proconio::input;

fn main() {
    input! {
        n: usize,
    }
    let mut dp = vec![1; n + 1];

    for i in 2..dp.len() {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    println!("{}", dp[n]);
}