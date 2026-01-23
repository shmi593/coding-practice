import sys
import queue

R, C = tuple(map(int, sys.stdin.readline().split()))
sy, sx = tuple(map(int, sys.stdin.readline().split()))
gy, gx = tuple(map(int, sys.stdin.readline().split()))

board = [sys.stdin.readline() for _ in range(R)]

within_board = lambda y, x: 0 < y <= R and 0 < x <= C
equals_to_goal = lambda y, x: y == gy and x == gx


def find_next_spaces(y, x, board):
    arounds = map(lambda d: (y + d[0], x + d[1]), [(-1, 0), (0, -1), (1, 0), (0, 1)])
    return tuple(
        filter(
            lambda n: within_board(n[0], n[1]) and board[n[0] - 1][n[1] - 1] == ".",
            arounds,
        )
    )


def bfs(q, board):
    moves = 0
    while not q.empty():
        y, x, moves = q.get()
        if equals_to_goal(y, x):
            return moves
        for ny, nx in find_next_spaces(y, x, board):
            board[ny - 1] = board[ny - 1][: nx - 1] + "#" + board[ny - 1][nx:]
            q.put((ny, nx, moves + 1))
    return moves


q = queue.Queue()
q.put((sy, sx, 0))
print(bfs(q, board))
