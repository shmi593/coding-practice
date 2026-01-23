from sys import stdin

listmap = lambda func, l: list(map(func, l))
to_int_list = lambda str_list: listmap(int, str_list) 

def get_combinations(m):
    combinations = []
    for i in range(m):
        for j in range(i + 1, m):
            combinations.append((i, j))
    return combinations

def choose_high_score(song1, song2):
    return lambda score: max(score[song1], score[song2])

def solve(scores, combinations):
    chosen_scores_total_list = []
    for song1, song2 in combinations:
        chosen_score_total = sum(listmap(choose_high_score(song1, song2), scores))
        chosen_scores_total_list.append(chosen_score_total)
    return max(chosen_scores_total_list)

n, m = [int(s) for s in input().split()]
# 得点の2次元配列作成
scores = [to_int_list(stdin.readline().split()) for _ in range(n)]
combinations = get_combinations(m)

print(solve(scores, combinations))
