# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d
from sys import stdin

N, M = map(int, stdin.readline().split())

# 距離
D = [int(stdin.readline()) for _ in range(N)]
# 天候の悪さ
C = [int(stdin.readline()) for _ in range(M)]

dp = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 都市 i + 1 は j + 1日目以前に到達しなければならず、
        # かつ都市 (N - i) + 1 は (M - j) + 1日目以降にしか到達できない
        if i <= j and N - i <= M - j:
            if i == 0:
                dp[i][j] = D[i] * C[j]
            else:
                dp[i][j] = min(filter(lambda x: x != -1, dp[i - 1][:j])) + D[i] * C[j]

print(min(filter(lambda x: x != -1, dp[N - 1])))
