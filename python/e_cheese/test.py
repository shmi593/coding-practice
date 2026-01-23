import sys
from collections import deque


def find_section(target, sections):
    str_section = str(target)
    for y, row in enumerate(sections):
        x = row.find(str_section)
        if not x == -1:
            return (y, x)


def solve():
    def bfs(sy, sx, gy, gx):
        q = deque()
        q.append((sy, sx, 0))
        visited = [[False] * W for _ in range(H)]
        while q:
            y, x, moves = q.popleft()
            if y == gy and x == gx:
                return moves
            for dy, dx in directions:
                ny, nx = (y + dy, x + dx)
                if not (0 <= ny < H and 0 <= nx < W):
                    continue
                if sections[ny][nx] == "X":
                    continue
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, moves + 1))

    H, W, N = tuple(map(int, sys.stdin.readline().split()))
    sections = [sys.stdin.readline() for _ in range(H)]
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    ans = 0
    sy, sx = find_section("S", sections)
    for i in range(N):
        gy, gx = find_section(i + 1, sections)
        ans += bfs(sy, sx, gy, gx)
        sy, sx = (gy, gx)

    return ans


print(solve())
