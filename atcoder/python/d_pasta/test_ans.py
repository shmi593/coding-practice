N, K = map(int, input().split())
AB = [map(int, input().split()) for _ in range(K)]

dp = [[[0] * 2 for _ in range(3)] for _ in range(N + 1)]

pasta = [-1] * (N + 1)

for a, b in AB:
    pasta[a] = b - 1

if pasta[1] != -1:
    dp[1][pasta[1]][0] = 1
else:
    for i in range(3):
        dp[1][i][0] = 1

for i in range(2, N + 1):
    for j in range(3):
        if pasta[i] != -1 and pasta[i] != j:
            dp[i][j][0], dp[i][j][1] = 0, 0
        else:
            for k in range(3):
                if j == k:
                    dp[i][j][1] += dp[i - 1][k][0]
                else:
                    dp[i][j][0] += dp[i - 1][k][0]
                    dp[i][j][0] += dp[i - 1][k][1]

ans = 0
for i in range(3):
    for j in range(2):
        ans += dp[N][i][j]

print(ans % 10000)
