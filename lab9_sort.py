
"""
Ввести масив А. 
У масив В перенести всі елементи масиву А, 
що стоять між мінімальним і максимальним елементами. 
Масив В впорядкувати за зростанням.
"""

import random

def quick_sort(array, p = 0, q = None):
  if q is None:
    q = len(array) - 1

  if p >= q:
    return
  i = partition(array, p, q)
  quick_sort(array, p, i - 1)
  quick_sort(array, i + 1, q)

def partition(array, p, q):
  i = p - 1
  x = array[q]

  for j in range(p , q): 
    if array[j] <= x: 
      i += 1 
      array[i], array[j] = array[j], array[i] 
  array[i+1], array[q] = array[q], array[i+1] 
  return i + 1


n = int(input('Розмір масиву:'))
A = [random.randint(0, 100) for _ in range(n)]

print(A)
index1, index2 = A.index(min(A)), A.index(max(A))
if index1 > index2:
  index1, index2 = index2, index1
B = A[index1+1:index2]

print('-' * 10)
print(B)

quick_sort(B)

print('-' * 10)
print(B)
