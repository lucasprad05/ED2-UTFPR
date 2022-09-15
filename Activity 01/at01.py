#Activity 01
#Lucas Prado & Erik Noda
#Data Structures 2

import sys
import time
import random

#Heap Sort
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
    start_time = time.time()
    compare = 0
    for i in range(len(array), -1, -1):
        heapify(array, len(array), i)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    end_time = time.time()
    return compare, (end_time - start_time)/1000

#Quick Sort
def quickSort(array):
    start_time = time.time()
    compare = 0
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
    end_time = time.time()
    return compare, (end_time - start_time)/1000

#Merge Sort
def mergeSort(array):
    start_time = time.time()
    compare = 0
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    end_time = time.time()
    return compare, (end_time - start_time)/1000

#Insertion Sort
def insertionSort(array, n):
    start_time = time.time()
    compare = 0
    for i in range(1, n):
        aux = array[i]
        j = i - 1
        while j >= 0 and aux < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = aux  
    end_time = time.time()
    return compare, (end_time - start_time)/1000

#Selection Sort
def selectionSort(array, n):
    start_time = time.time()
    compare = 0
    n -= 1
    for i in range(n):
        aux = i
        for j in range(i, n):
            if array[j] < array[aux]:
                aux = j
        if aux != array[i]:
            array[aux], array[i] = array[i], array[aux]
    end_time = time.time()
    return compare, (end_time - start_time)/1000

#Bubble Sort
def bubbleSort(array, n):
    start_time = time.time()
    compare = 0
    change = True
    while change == True:
        change = False
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change = True
    end_time = time.time()
    return compare, (end_time - start_time)/1000

#Main
option = 'r'#c d ou s ler do ARQUIVO
N = 5 #tamanho do vetor
array = list(range(N))

if option == 'c':
    for i in range(N):
        array[i] = i + 1
    print(array)
elif option == 'd':
    #d
    aux = N
    for i in range(N):
        array[i] = aux
        aux -=1
    print(array)
elif option == 'r':
    #random
    for i in range(N):
        array[i] = random.randint(0, 32000)
    print(array)
else:
    print('Opção inválida!')

#Sorts
insertionSort(array, len(array))
print('Insertion: ', array)

selectionSort(array, len(array))
print('Selection: ', array)

bubbleSort(array, len(array))
print('Bubble: ', array)

mergeSort(array)
print('Merge: ', array)

quickSort(array)
print('Quick: ', array)

heapSort(array)
print('Heap: ', array)