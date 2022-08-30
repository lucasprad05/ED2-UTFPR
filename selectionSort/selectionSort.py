#Selection Sort
#Lucas Prado & Erik Noda
#Data Structures 2

def selectionSort(v):
    n = len(v)
    n -= 1
    for i in range(n):
        aux = i

        for j in range(i, n):
            if v[j] < v[aux]:
                aux = j
        
        if aux != v[i]:
            v[aux], v[i] = v[i], v[aux]

    print(v)

v = [-19, -61, -36, 36, -48, 32, -9, 16, -34, -77, 80, -26, -18, -27, 84]
selectionSort(v)