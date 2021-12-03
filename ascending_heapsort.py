def left_child(index):
    return index * 2 + 1


def right_child(index):
    return index * 2 + 2


def max_heapify(arr, index, heapsize):
    left = left_child(index)
    right = right_child(index)

    largest = index

    if left < heapsize and arr[left] > arr[index]:
        largest = left

    if right < heapsize and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]

        max_heapify(arr, largest, heapsize)


def build_max_heap_tree(arr, heapsize):
    for i in range(len(arr)-1//2, -1, -1):
        max_heapify(arr, i, heapsize)


def heapsort(arr, heapsize):
    build_max_heap_tree(arr, heapsize)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapsize = i
        max_heapify(arr, 0, heapsize)


arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
heapsort(arr, len(arr))
print(arr)
