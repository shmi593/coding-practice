import sys
import copy

sys.setrecursionlimit(10**8)

# input
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

valid_field = lambda h, w: 0 <= h < n and 0 <= w < m

d_blocks = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dfs(h, w, ices=1):
    temp_fields[h][w] = 0
    # 周囲4マスを探索
    for dh, dw in d_blocks:
        nh = h + dh
        nw = w + dw
        if valid_field(nh, nw) and temp_fields[nh][nw]:
            ices += 1
            return dfs(nh, nw, ices)
    return ices


ans = 0
for h in range(n):
    for w in range(m):
        if fields[h][w]:
            temp_fields = copy.deepcopy(fields)
            ans = max(ans, dfs(h, w, 1))

print(ans)
