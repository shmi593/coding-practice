# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
from sys import stdin

N, K = map(int, stdin.readline().split())

# すでに決まっているパスタの日付を記録
decided = [-1 for _ in range(N)]
for _ in range(K):
    d, k = map(int, stdin.readline().split())
    decided[d - 1] = k - 1

# i日目にj番目のパスタを食べる組み合わせの数を場合分けして持っておく
# dp[i][j][0]: i-1日目にj番目のパスタを食べない場合
# dp[i][j][1]: i-1日目にj番目のパスタを食べる場合
dp = [[[0, 0] for _ in range(3)] for _ in range(N)]

# 1日目の場合分け
# 1日目に決まっているパスタがない場合
if decided[0] == -1:
    dp[0] = [[1, 0] for _ in range(3)]
# 1日目に決まっているパスタがある場合
else:
    dp[0][decided[0]] = [1, 0]

for i in range(1, N):
    # i日目にj番目のパスタを食べる組み合わせの数を計算
    for j in range(3):
        # i - 1日目にj番目のパスタを食べない場合の組み合わせ数
        # -> dp[i - 1][<not j>] の組み合わせ数の合計
        dp[i][j][0] = sum(dp[i - 1][(j + 1) % 3]) + sum(dp[i - 1][(j + 2) % 3])
        # i - 1日目にj番目のパスタを食べる場合の組み合わせ数
        # -> dp[i - 1][j][0] (i-2日目に j番目以外のパスタを食べ、i-1日目にj番目のパスタを食べる場合の組み合わせ数)
        dp[i][j][1] = dp[i - 1][j][0]

        dp[i][j][0] %= 10000
        dp[i][j][1] %= 10000

    # i日目に食べるパスタが決まっている場合、別のパスタは食べないとわかるので、i日目の別のパスタの組み合わせ数を0にする
    if decided[i] != -1:
        dp[i][(decided[i] + 1) % 3] = [0, 0]
        dp[i][(decided[i] + 2) % 3] = [0, 0]

flatten_dp_N = sum(dp[N - 1], [])
ans = sum(flatten_dp_N) % 10000
print(ans)
