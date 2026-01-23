import sys


def bfs(adjacency_set, depth=0):
    if len(adjacency_set) == 0:
        return
    next_adjacency_set = set()
    depth += 1
    for u in adjacency_set:
        checked[u - 1] = True
        ans_list[u - 1] = (u, depth)
        next_adjacency_set |= {
            nu for nu in all_adjacency_list[u - 1] if not checked[nu - 1]
        }
    bfs(next_adjacency_set, depth)


n = int(input())

# 隣接ノードリスト
all_adjacency_list = [set() for _ in range(n)]
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    if not row[1] == 0:
        all_adjacency_list[row[0] - 1] = set(row[-row[1] :])

# 探索済み
checked = [True if i == 0 else False for i in range(n)]

ans_list = [(u, 0) if u == 1 else (u, -1) for u in range(1, n + 1)]

bfs(all_adjacency_list[0])

for ans in ans_list:
    print(*ans)
