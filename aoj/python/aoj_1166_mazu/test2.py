from collections import deque


def within_map(y, x):
    return 0 <= y < h and 0 <= x < w


def find_next(y, x):
    return [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]


def bfs(mazu, h, w):
    q = deque()
    q.append((0, 0))
    visited = [[False] * w for _ in range(h)]
    moves = 1
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            for ny, nx in find_next(y, x):
                if not within_map(ny, nx) or visited[ny][nx]:
                    continue
                if ny == h - 1 and nx == w - 1:
                    return moves
                if (y + ny) % 2 == 0:
                    if mazu[(y + ny) // 2][x // 2] == 1:
                        continue
                else:
                    if mazu[y // 2][(x + nx) // 2] == 1:
                        continue
                q.append((ny, nx))
                visited[ny][nx] = True
        moves += 1
    return 0


# マップの入力
h, w = map(int, input().split())
mazu = []
for i in range(h):
    row = input().strip()
    if i % 2 == 0:
        mazu.append([int(row[j]) for j in range(1, 2 * w, 2)])
    else:
        mazu.append([int(row[j]) for j in range(0, 2 * w + 1, 2)])

result = bfs(mazu, h, w)
if result == 0:
    print(result)
else:
    print(result + 1)
