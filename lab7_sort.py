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
  max_ = arr[i][-2]
  index = i
  for j in range(i+1, n):
    if arr[j][-2] > max_:
      max_ = arr[j][-2]
      index = j
  if arr[i][-2] < arr[index][-2]:
    arr[i][-2], arr[index][-2] = arr[index][-2], arr[i][-2]

print('-' * 10)

print_matrix(arr)
