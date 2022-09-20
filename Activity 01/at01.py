#Activity 01
#Lucas Prado & Erik Noda
#Data Structures 2

import sys
from time import time
import random

#Heap Sort
def heapify(array, n, i):
    compare = 0
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    compare += 1
    if l < n and array[i] < array[l]:
        largest = l
    compare += 1
    if r < n and array[largest] < array[r]:
        largest = r
    compare += 1
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)
    return compare

def heapSort(array):
    compare = 0
    for i in range(len(array), -1, -1):
        compare = heapify(array, len(array), i)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        compare = heapify(array, i, 0)
    return compare

#Quick Sort
def quickSort(array):
    compare = 0
    if len(array) > 1:
        pivot = array[0]
        less = []
        greater = []
        for i in range(1, len(array)):
            compare += 1
            if array[i] < pivot:
                less.append(array[i])
            else:
                greater.append(array[i])
        quickSort(less)
        quickSort(greater)
        array[:] = less + [pivot] + greater
    return compare

#Merge Sort
def mergeSort(array):
    compare = 0
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            compare += 1
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
    return compare

#Insertion Sort
def insertionSort(array, n):
    compare = 0
    for i in range(1, n):
        aux = array[i]
        j = i - 1
        compare += 1
        while j >= 0 and aux < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = aux
    return compare

#Selection Sort
def selectionSort(array, n):
    compare = 0
    n -= 1
    for i in range(n):
        aux = i
        for j in range(i, n):
            compare += 1
            if array[j] < array[aux]:
                aux = j
        compare += 1
        if aux != array[i]:
            array[aux], array[i] = array[i], array[aux]
    return compare

#Bubble Sort
def bubbleSort(array, n):
    compare = 0
    change = True
    while change == True:
        change = False
        for i in range(n - 1):
            compare += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change = True
    return compare

#Main
option = 'r'#c d ou s ler do ARQUIVO
N = 5 #tamanho do vetor
array = list(range(N))

if option == 'c':
    for i in range(N):
        array[i] = i + 1
    #print(array)
elif option == 'd':
    #d
    aux = N
    for i in range(N):
        array[i] = aux
        aux -=1
    #print(array)
elif option == 'r':
    #random
    for i in range(N):
        array[i] = random.randint(0, 32000)
    #print(array)
else:
    print('Opção inválida!')

#Sorts
comp = 0

for i in range (6):
    if i == 0:
        start = time()
        comp = insertionSort(array, len(array))
        end = time()
        time = (end - start) * 1000
        print('insertionSort: ', array, comp, 'comp', time, 'ms')

    elif i == 1:
        comp = selectionSort(array, len(array))
        print('selectionSort: ', array, comp, 'comp', 'ms')

    elif i == 2:
        comp = bubbleSort(array, len(array))
        print('bubbleSort: ', array, comp, 'comp', 'ms')

    elif i == 3:
        comp = mergeSort(array)
        print('mergeSort: ', array, comp, 'comp', 'ms')
    
    elif i == 4:
        comp = quickSort(array)
        print('quickSort: ', array, comp, 'comp',  'ms')
    
    elif i == 5:
        comp = heapSort(array)
        print('heapSort: ', array, comp, 'comp', 'ms')
