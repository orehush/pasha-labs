"""
Дано квадратну матрицю розмірності n×n.
Надрукувати елементи передостаннього стовпця у порядку спадання.
"""

import random


def print_matrix(array):
    for arr in array:
        print(arr)

n = int(input('Розмір матриці:'))
arr = [[random.randint(0, 100) for _ in range(n)] for i in range(n)]

print_matrix(arr)

for i in range(n):
    col = [arr[j][-2] for j in range(i, n)]
    m = min(col)
    index = col.index(m)
    if arr[i][-2] < arr[index+i][-2]:
        arr[i][-2], arr[index + i][-2] = arr[index+i][-2], arr[i][-2]

print('-'*10)

print_matrix(arr)
# for i in range(n):
#     for j in range(i, n):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#
# print(arr)
# print(arr[0] + arr[-1])
