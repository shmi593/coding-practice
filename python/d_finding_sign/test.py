from sys import stdin

m = int(input())
stars = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
s_stars = set(stars)
n = int(input())
photo_stars = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

for x1, y1 in photo_stars:
    dx = x1 - stars[0][0]
    dy = y1 - stars[0][1]
    found = 0
    for x2, y2 in photo_stars:
        if (x2 - dx, y2 - dy) in s_stars:            
            found += 1
    if found == m:
        print(dx, dy)
        exit()
