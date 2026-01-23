from queue import Queue

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    vl = list()
    hl = list()
    for i in range(h * 2 - 1):
        if i % 2:
            hl.append(list(map(int, input().split())))
        else:
            vl.append(list(map(int, input().split())))

    q = Queue()
    d = [[-1 for _ in range(h)] for _ in range(w)]
    q.put((0, 0))
    d[0][0] = 1
    while not q.empty():
        x, y = q.get()

        if x > 0 and (not vl[y][x - 1]) and d[x - 1][y] == -1:
            d[x - 1][y] = d[x][y] + 1
            q.put((x - 1, y))

        if x < w - 1 and (not vl[y][x]) and d[x + 1][y] == -1:
            d[x + 1][y] = d[x][y] + 1
            q.put((x + 1, y))

        if y > 0 and (not hl[y - 1][x]) and d[x][y - 1] == -1:
            d[x][y - 1] = d[x][y] + 1
            q.put((x, y - 1))

        if y < h - 1 and (not hl[y][x]) and d[x][y + 1] == -1:
            d[x][y + 1] = d[x][y] + 1
            q.put((x, y + 1))

    if d[w - 1][h - 1] == -1:
        print(0)
    else:
        print(d[w - 1][h - 1])
