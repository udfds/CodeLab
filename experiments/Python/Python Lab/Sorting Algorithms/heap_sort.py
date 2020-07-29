def heapify(array, size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and array[index] < array[left]:
        largest = left
    if right < size and array[largest] < array[right]:
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, size, largest)


def heap_sort(array):
    size = len(array)
    for index in range(size//2 - 1, -1, -1):
        heapify(array, size, index)
    for index in range(size - 1, 0, -1):
        array[index], array[0] = array[0], array[index]
        heapify(array, index, 0)


if __name__ == '__main__':
    array = [19, 50, 27, 7, 2020, 14, 18, 1, 12, 23, 200, 2201]
    heap_sort(array)
    print(array)
