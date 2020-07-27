def _quick_sort_partition(array, low, hight):
    index_i = (low - 1)
    pivot = array[hight]

    for index_j in range(low, hight):
        if array[index_j] < pivot:
            index_i = index_i + 1
            array[index_i], array[index_j] = array[index_j], array[index_i]
    array[index_i + 1], array[hight] = array[hight], array[index_i + 1]
    return (index_i + 1)


def quick_sort(array, low, hight):
    if low < hight:
        index = _quick_sort_partition(array, low, hight)
        quick_sort(array, low, index - 1)
        quick_sort(array, index + 1, hight)


if __name__ == '__main__':
    array = [19, 50, 27, 7, 2020, 14, 18, 1, 12, 23, 200, 2201]
    quick_sort(array, 0, len(array) - 1)
    print(array)
