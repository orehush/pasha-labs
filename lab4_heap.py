def max_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    largest = i
    if left <= length and array[left] > array[i]:
        largest = left
    if right <= length and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)


def build_max_heap(array):
    for i in reversed(range(len(array)//2)):
        max_heapify(array, i)


def print_heap(array):
    row = 0
    index = 0
    cnt = 1
    while index < len(array):
        print(array[index], end=' ')
        if cnt == index + 1:
            row += 1
            cnt += 2**row
            print()
        index += 1

if __name__ == '__main__':
    arr = [4, 5, 4, 78, 43, 56, 21, 67, 33, 56, 87, 5, 44]
    build_max_heap(arr)
    print(arr)
    print_heap(arr)
