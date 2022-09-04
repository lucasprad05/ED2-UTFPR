#Insertion Sort
#Lucas Prado & Erik Noda
#Data Structures 2

def insertionSort(v, n):
    for i in range(1, n):
        aux = v[i]
        j = i - 1
        while j >= 0 and aux < v[j]:
            v[j+1] = v[j]
            j = j - 1
        v[j+1] = aux  
    print(v)

v = [-19, -61, -36, 36, -48, 32, -9, 16, -34, -77, 80, -26, -18, -27, 84]
insertionSort(v, len(v))