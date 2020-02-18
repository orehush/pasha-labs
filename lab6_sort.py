"""
Відсортувати масив А з n елементів в порядку зростання
та знайти суму першого та останнього елементів масиву.
"""

import random

n = int(input('Розмір масиву:'))
arr = [random.randint(0, 100) for _ in range(n)]

print(arr)

for i in range(n):
    for j in range(i, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
print(arr[0] + arr[-1])
