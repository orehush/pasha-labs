"""
Дано квадратну матрицю розмірності n× n. 
Надрукувати елементи бічної діагоналі у порядку спадання.
"""

import random


def print_matrix(array):
  for arr in array:
    print(arr)

n = int(input('Розмір матриці:'))
arr = [[random.randint(0, 100) for _ in range(n)] for i in range(n)]

print_matrix(arr)

arr2 = [arr[i][-i-1] for i in range(n)]

print('-' * 10)
print(arr2)

for i in range(1, n):
  temp = arr2[i]
  j = i - 1
  while j >= 0 and temp > arr2[j]:
    arr2[j + 1] = arr2[j]
    j = j - 1
  arr2[j + 1] = temp

print('-' * 10)
print(arr2)
