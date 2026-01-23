from sys import stdin

m = int(input())
stars = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
n = int(input())
photo_stars = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

print(n)
# print(photo_stars)