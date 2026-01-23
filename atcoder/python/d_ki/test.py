import sys

sys.setrecursionlimit(10**6)

N, Q = [int(s) for s in sys.stdin.readline().split()]

to_index = lambda s: int(s) - 1


def dfs(i):
    for node in tree[i]:
        if visited[node]:
            continue
        ans[node] += ans[i]
        visited[i] = True
        dfs(node)


tree, visited, ans = [], [], []
for _ in range(N):
    tree.append([])
    visited.append(False)
    ans.append(0)

for _ in range(N - 1):
    a, b = tuple(map(to_index, sys.stdin.readline().split()))
    tree[a].append(b)
    tree[b].append(a)

for _ in range(Q):
    p, x = tuple(map(int, sys.stdin.readline().split()))
    ans[p - 1] += x

dfs(0)
print(*ans)
