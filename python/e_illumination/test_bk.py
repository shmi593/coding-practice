from sys import stdin
from collections import deque

within_map = lambda y, x: 0 <= y < H and 0 <= x < W

directions_odd = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
directions_even = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]


def find_next(y, x):
    arounds = map(
        lambda d: (y + d[0], x + d[1]),
        directions_even if y % 2 == 0 else directions_odd,
    )
    return tuple(
        filter(
            lambda t: within_map(*t),
            arounds,
        )
    )


def is_kado(y, x):
    return any(
        map(
            lambda t: y == t[0] and x == t[1],
            [(0, 0), (H - 1, 0), (0, W - 1), (H - 1, W - 1)],
        )
    )


def is_haji(y, x):
    return any([y == 0, y == H - 1, x == 0, x == W - 1])


def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    illumination = 0
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        next = find_next(y, x)
        if (
            imap[y][x] == 0
            and len(next) == 6
            and all(map(lambda t: imap[t[0]][t[1]] == 1, next))
        ):
            illumination -= 6
        if imap[y][x] == 1:
            if (y + x) % 2 == 0:
                if is_kado(y, x):
                    illumination += 3
                elif y == 0 or y == (H - 1):
                    illumination += 2
                else:
                    illumination += 1
            else:
                if is_kado(y, x):
                    illumination += 4
                elif y == 0 or y == (H - 1):
                    illumination += 2
                else:
                    illumination += 3
        for ny, nx in next:
            if visited[ny][nx]:
                continue
            if imap[y][x] + imap[ny][nx] == 1:
                illumination += 1
            q.append((ny, nx))
        print(y, x, illumination)
    return illumination


W, H = tuple(map(int, stdin.readline().split()))
imap = [list(map(int, stdin.readline().split())) for _ in range(H)]
visited = [[False] * W for _ in range(H)]

print(bfs(0, 0))
