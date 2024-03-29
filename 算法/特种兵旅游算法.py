import numpy as np
from itertools import permutations

# 1. 创建一个20x20的距离矩阵，随机初始化，对角线元素为0。
n = 20
distances = np.random.rand(n, n) * 100
np.fill_diagonal(distances, 0)

# 2. 使用动态规划解决旅行商问题，找到可以游览五个景点的最短行程路线。
def tsp(distances, num_spots):
    # 生成所有可能的行程
    tours = permutations(range(num_spots))
    min_tour = None
    min_distance = float('inf')

    for tour in tours:
        distance = 0
        for i in range(num_spots - 1):
            distance += distances[tour[i]][tour[i+1]]
        distance += distances[tour[-1]][tour[0]]  # 返回起点
        if distance < min_distance:
            min_distance = distance
            min_tour = tour

    return min_tour, min_distance

min_tour, min_distance = tsp(distances, 5)
print(f"可以游览五个景点的最短行程路线为：{min_tour}，总距离为：{min_distance}")