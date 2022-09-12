#Heap Sort
#Lucas Prado & Erik Noda
#Data Structures 2

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heapSort(array):
    for i in range(len(array), -1, -1):
        heapify(array, len(array), i)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

v = [-19, -61, -36, 36, -48, 32, -9, 16, -34, -77, 80, -26, -18, -27, 84]
heapSort(v)
print(v)