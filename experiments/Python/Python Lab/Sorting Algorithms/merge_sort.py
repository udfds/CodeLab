def merger_sort(array):
    length = len(array)

    if length > 1:
        mid = length//2
        array_left = array[:mid]
        array_right = array[mid:]

        merger_sort(array_left)
        merger_sort(array_right)

        index_i = 0
        index_j = 0
        index_k = 0

        while index_i < len(array_left) and index_j < len(array_right):
            if array_left[index_i] < array_right[index_j]:
                array[index_k] = array_left[index_i]
                index_i += 1
            else:
                array[index_k] = array_right[index_j]
                index_j += 1
            index_k += 1

        while index_i < len(array_left):
            array[index_k] = array_left[index_i]
            index_i += 1
            index_k += 1

        while index_j < len(array_right):
            array[index_k] = array_right[index_j]
            index_j += 1
            index_k += 1


if __name__ == '__main__':
    array = [19, 50, 27, 7, 2020, 14, 18, 1, 12, 23, 200, 2201]
    merger_sort(array)
    print(array)
