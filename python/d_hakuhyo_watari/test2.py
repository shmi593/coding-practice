import sys

sys.setrecursionlimit(10**8)
m = int(input())
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]


dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
maxn = 0


def dfs(x, y, c):
    global depth
    visited[y][x] = True
    if c > depth:
        depth += 1
    print(f"x={x}, y={y}, c={c}, depth={depth}")
    for dx, dy in dirc:
        nex = x + dx
        ney = y + dy
        if 0 <= nex < m and 0 <= ney < n:
            if visited[ney][nex] == False and g[ney][nex] == 1:
                print(f"next: ({nex}, {ney})")
                dfs(nex, ney, c + 1)

    visited[y][x] = False


for i in range(n):
    for j in range(m):
        visited = [[False for _ in range(m)] for _ in range(n)]
        if g[i][j] == 1:
            depth = 0
            dfs(j, i, 1)
            maxn = max(maxn, depth)

print(maxn)
