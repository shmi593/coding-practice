from sys import stdin

to_float = lambda arr: map(float, arr)

# 行列の積: n行1列の行列を生成
# a: l行n列, b: n行1列
def dot_n1(n, l):
    return lambda a, b: [sum([a[i][j]*b[j] for j in range(l)]) for i in range(n)]

# 2行1列の行列を生成
dot_21 = dot_n1(2, 2)

# x' - a   cosΘ  -sinΘ    x - a
#        =              × 
# y' - b   sinΘ   cosΘ    y - b
# 回転後の座標を求める
def apply_rotation_matrix(rotation_matrix):
    def calc_rotated_coordinate(origin_matrix, p1):
        return tuple([a + b for (a, b) in zip(dot_21(rotation_matrix, origin_matrix), p1)])
    return calc_rotated_coordinate

# 45度反時計回りに回転して √2 で割る
calc_45_rotated_and_division_root_2_coordinate = apply_rotation_matrix(((0.5, -0.5), (0.5, 0.5)))
# 45度時計回りに回転 √2 で割る
calc_minus_45_rotated_and_division_root_2_coordinate = apply_rotation_matrix(((0.5, 0.5), (-0.5, 0.5)))

# 面積計算
calc_area = lambda distance: (distance[0] ** 2  + distance[1] ** 2) / 2

xy_distance = lambda p1, p2: (p2[0] - p1[0], p2[1] - p1[1])

# 第一象限の座標かつ整数の座標か？
def is_first_quadrant_and_integer(coordinates):
    for coordinate in coordinates: 
        for n in coordinate:
            if not n.is_integer() or n < 0:
                return False
    return True

n = int(input())
coordinates = sorted([tuple(to_float(stdin.readline().split())) for _ in range(n)], key=lambda k: [k[1], k[0]])
s_coordinates = set(coordinates)
ans = 0
# p1, p2 は対角, 辺 p1-p2 は対角線になる
# 辺 p1-p2 を 時計回り, 反時計回りに 45度 回転させ、長さを 1 / √2 倍した座標 p3, p4 があるか探す
for i in range(0, n - 3):
    p1 = coordinates[i]
    for j in reversed(range(i + 1, n)):
        p2 = coordinates[j]
        distance = xy_distance(p1, p2)
        area = calc_area(distance)
        if area <= ans:
            continue
        p3_p4 = {
            calc_45_rotated_and_division_root_2_coordinate(distance, p1),
            calc_minus_45_rotated_and_division_root_2_coordinate(distance, p1)
        }
        if is_first_quadrant_and_integer(p3_p4):
            # p3_p4 が s_coordinates の部分集合か？
            if p3_p4 <= s_coordinates:
                ans = area
print(int(ans))
