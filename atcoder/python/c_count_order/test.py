from sys import stdin
import itertools

def solve(N, P, Q):
    numbers = [i for i in range(1, N + 1)]
    # itertools.permutations is sorted
    # https://docs.python.org/3.8/library/itertools.html#itertools.permutations
    pl = list(itertools.permutations(numbers, len(numbers)))
    return abs(pl.index(P) - pl.index(Q))

N = int(input())
P = tuple(map(int, (stdin.readline().split())))
Q = tuple(map(int, (stdin.readline().split())))

print(solve(N, P, Q))
