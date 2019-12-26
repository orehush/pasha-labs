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

arr_col = [arr[i][-2] for i in range(n)]

for i in range(n):
  max_ = arr_col[i]
  index = i
  for j in range(i+1, n):
    if arr_col[j] > max_:
      max_ = arr_col[j]
      index = j
  if arr_col[i] < arr_col[index]:
    arr_col[i], arr_col[index] = arr_col[index], arr_col[i]

print('-' * 10)
print(arr_col)
