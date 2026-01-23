import sys

sys.setrecursionlimit(10**7)  # 再帰回数の上限変更


def setup(max_h):
    arr = []
    for h in range(max_h):
        arr.append(list(map(int, sys.stdin.readline().split())))
    return arr


def dfs(h, w):
    island_blocks[h][w] = 0
    # 該当マスの周囲8マスを探索
    for nh in range(max(h - 1, 0), min(h + 2, len(island_blocks))):
        for nw in range(max(w - 1, 0), min(w + 2, len(island_blocks[nh]))):
            if island_blocks[nh][nw] == 1:
                dfs(nh, nw)
    return


while True:
    w, h = [int(s) for s in sys.stdin.readline().split()]
    if w == 0 and h == 0:
        break

    island_blocks = setup(h)
    n_lands = 0
    for h, row in enumerate(island_blocks):
        for w, is_land in enumerate(row):
            if is_land:
                dfs(h, w)
                n_lands += 1
    print(n_lands)
