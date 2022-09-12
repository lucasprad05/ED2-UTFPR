#Quick Sort
#Lucas Prado & Erik Noda
#Data Structures 2

def quickSort(array):
    if len(array) > 1:
        pivot = array[0]
        less = []
        greater = []
        for i in range(1, len(array)):
            if array[i] < pivot:
                less.append(array[i])
            else:
                greater.append(array[i])
        quickSort(less)
        quickSort(greater)
        array[:] = less + [pivot] + greater

v = [-19, -61, -36, 36, -48, 32, -9, 16, -34, -77, 80, -26, -18, -27, 84]
quickSort(v)
print(v)