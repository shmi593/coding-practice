# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d
from sys import stdin

D, N = map(int, stdin.readline().split())

tempratures = [int(stdin.readline()) for _ in range(D)]
clothes = [list(map(int, stdin.readline().split())) for _ in range(N)]

dp = [[-1 for _ in range(N)] for _ in range(D)]

for i in range(D):
    for j in range(N):
        if clothes[j][0] <= tempratures[i] <= clothes[j][1]:
            if i == 0:
                dp[i][j] = 0
            else:
                for k in range(N):
                    if dp[i - 1][k] == -1:
                        continue
                    dp[i][j] = max(
                        dp[i][j], dp[i - 1][k] + abs(clothes[j][2] - clothes[k][2])
                    )

print(max(dp[D - 1]))
