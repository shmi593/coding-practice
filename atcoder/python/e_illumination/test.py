from sys import stdin
from collections import deque

within_map = lambda y, x: 0 <= y < H + 2 and 0 <= x < W + 2

directions_odd = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
directions_even = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]


def find_next(y, x):
    return map(
        lambda d: (y + d[0], x + d[1]),
        directions_even if y % 2 == 0 else directions_odd,
    )


def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    illumination = 0
    while q:
        y, x = q.popleft()
        for ny, nx in find_next(y, x):
            if not within_map(ny, nx) or visited[ny][nx]:
                continue
            if imap[ny][nx] == 1:
                illumination += 1
                continue
            visited[ny][nx] = True
            q.append((ny, nx))
    return illumination


W, H = tuple(map(int, stdin.readline().split()))
imap = (
    [[0] * (W + 2)]
    + [[0] + list(map(int, stdin.readline().split())) + [0] for _ in range(H)]
    + [[0] * (W + 2)]
)
visited = [[False] * (W + 2) for _ in range(H + 2)]

print(bfs(0, 0))
