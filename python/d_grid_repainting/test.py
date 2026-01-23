from sys import stdin
from collections import deque

within_map = lambda y, x: 0 <= y < H and 0 <= x < W
out_of_map = lambda y, x: not within_map(y, x)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
find_next = lambda y, x: map(lambda d: (y + d[0], x + d[1]), directions)

is_wall = lambda y, x: board[y][x] == "#"

is_goal = lambda y, x: y == H - 1 and x == W - 1


def bfs():
    q = deque()
    q.append((0, 0))
    moves = [[-1] * W for _ in range(H)]
    moves[0][0] = 1
    while q:
        y, x = q.popleft()
        for ny, nx in find_next(y, x):
            # out of map or already visited
            if out_of_map(ny, nx) or moves[ny][nx] > 0:
                continue

            if is_wall(ny, nx):
                continue

            moves[ny][nx] = moves[y][x] + 1

            if is_goal(ny, nx):
                return moves[ny][nx]
            q.append((ny, nx))
    return -1


H, W = tuple(map(int, stdin.readline().split()))
board = [stdin.readline().rstrip() for _ in range(H)]
spaces = sum([row.count(".") for row in board])

distances = bfs()
if distances == -1:
    print(distances)
else:
    print(spaces - distances)
