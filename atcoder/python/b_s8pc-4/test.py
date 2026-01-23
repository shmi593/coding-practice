from sys import stdin

N, K = [int(s) for s in stdin.readline().split()]
a = [int(s) for s in stdin.readline().split()]

def prepare_patterns(N, K, a):
    if N == K:
        return [a]

    must_choose_building_indexes = [i for i in range(1, K) if max(a[:i]) < a[i]]
    contains_buildings = lambda i, buildings: all([i & 1 << b for b in buildings])
    patterns = []
    for i in range(1 << N):
        if not contains_buildings(i, must_choose_building_indexes):
            continue
        choices = a[:1] + [a[j] for j in range(1, N) if i & 1 << j]
        if len(choices) == K:
            patterns.append(choices)
    return patterns

patterns = prepare_patterns(N, K, a)
# solve
costs = set()
for current in patterns:
    after = current[:1]
    for i in range(1, len(current)):
        after.append(max(current[i], after[i - 1] + 1))
    cost = sum([max(a - c, 0) for c, a in zip(current, after)])
    costs.add(cost)

print(min(costs))
