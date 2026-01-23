from sys import stdin
import itertools
import math

def calc_distance(route):
    i = 0
    distance = 0
    for i in range(1, len(route)):
        distance += math.sqrt(
            (route[i][0] - route[i - 1][0]) ** 2
            + (route[i][1] - route[i - 1][1]) ** 2
        )
    return distance

def solve(coordinates):
    distances = []
    for route in list(itertools.permutations(coordinates, len(coordinates))):
        distances.append(calc_distance(route))
    return sum(distances) / len(distances)


N = int(input())
coordinates = [tuple(map(int, (stdin.readline().split()))) for _ in range(N)]

print(solve(coordinates))
