import sys
import queue
import copy


class Board:
    def __init__(self, height: int, width: int, sections: list):
        self.height = height
        self.width = width
        self.sections = copy.copy(sections)

    def cannot_move(self, y, x):
        return self.sections[y - 1][x - 1] == "X"

    def within_board(self, y, x):
        return 0 < y <= self.height and 0 < x <= self.width

    def is_target_section(self, y, x, target_section):
        return self.sections[y - 1][x - 1] == target_section

    def find_start(self, section):
        for sy, row in enumerate(self.sections, start=1):
            i = row.find(section)
            if not i == -1:
                return (sy, i + 1)

    def find_next(self, y, x):
        arounds = map(
            lambda n: (y + n[0], x + n[1]), [(-1, 0), (0, -1), (1, 0), (0, 1)]
        )
        return tuple(
            filter(
                lambda n: self.within_board(*n) and self.can_move(*n),
                arounds,
            )
        )

    def mark(self, y, x):
        self.sections[y - 1] = (
            self.sections[y - 1][: x - 1] + "X" + self.sections[y - 1][x:]
        )

    def reset_mark(self, initial_sections):
        self.sections = copy.copy(initial_sections)


def main():
    def bfs(sy, sx, next_section):
        q = queue.Queue()
        q.put((sy, sx, 0))
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while not q.empty():
            y, x, moves = q.get()
            board.mark(y, x)
            if board.is_target_section(y, x, next_section):
                return moves
            for dy, dx in directions:
                ny, nx = (y + dy, x + dx)
                if not board.within_board(ny, nx):
                    continue
                if board.cannot_move(ny, nx):
                    continue
                q.put((ny, nx, moves + 1))
        return moves + 1

    H, W, N = tuple(map(int, sys.stdin.readline().split()))
    initial_sections = [sys.stdin.readline() for _ in range(H)]
    board = Board(H, W, initial_sections)

    ans = 0
    for i in range(N):
        start_section = "S" if i == 0 else str(i)
        sy, sx = board.find_start(start_section)
        ans += bfs(sy, sx, str(i + 1))
        board.reset_mark(initial_sections)

    return ans


print(main())
