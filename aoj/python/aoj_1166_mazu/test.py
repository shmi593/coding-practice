from sys import stdin
from collections import deque

within_map = lambda y, x: 0 <= y < h and 0 <= x < w

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_next(y, x):
    return map(lambda d: (y + d[0], x + d[1]), directions)


def is_goal(y, x):
    return y == h - 1 and x == w - 1


def is_wall_func(vertical, horizontal):
    def _is_wall(y, x, ny, nx):
        return (
            (ny == y and nx == x + 1 and vertical[ny][nx - 1] == 1)  # right
            or (ny == y and nx == x - 1 and vertical[ny][nx] == 1)  # left
            or (ny == y + 1 and x == nx and horizontal[ny - 1][nx] == 1)  # down
            or (ny == y - 1 and x == nx and horizontal[ny][nx] == 1)  # up
        )

    return _is_wall


def bfs(mazu, h, w):
    q = deque()
    q.append((0, 0))
    vertical = mazu[::2]
    horizontal = mazu[1::2]
    is_wall = is_wall_func(vertical, horizontal)
    moves = [[-1] * w for _ in range(h)]
    moves[0][0] = 1
    while q:
        y, x = q.popleft()
        for ny, nx in find_next(y, x):
            # out of map or already visited
            if not within_map(ny, nx) or moves[ny][nx] != -1:
                continue

            if is_wall(y, x, ny, nx):
                continue

            moves[ny][nx] = moves[y][x] + 1

            if is_goal(ny, nx):
                return moves[ny][nx]
            q.append((ny, nx))
    return 0


while True:
    w, h = tuple(map(int, stdin.readline().split()))
    if w == 0 and h == 0:
        break
    mazu = [list(map(int, stdin.readline().split())) for _ in range(2 * h - 1)]
    print(bfs(mazu, h, w))
