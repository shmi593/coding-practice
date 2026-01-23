# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d
from sys import stdin

N = int(stdin.readline())

S = [list(stdin.readline().strip()) for _ in range(5)]
# 行列を反転しつつ、列ごとに文字列を連結
S = list(map(lambda t: "".join(t), zip(*S)))

# ['W', 'B', 'R'] の順に塗るコストを記録
dp = [[0 for _ in range(3)] for _ in range(N + 1)]

for i, col in enumerate(S):
    dp[i + 1][0] = min(dp[i][1], dp[i][2]) + sum(1 for c in col if c != "W")
    dp[i + 1][1] = min(dp[i][0], dp[i][2]) + sum(1 for c in col if c != "B")
    dp[i + 1][2] = min(dp[i][0], dp[i][1]) + sum(1 for c in col if c != "R")

print(min(dp[N]))
