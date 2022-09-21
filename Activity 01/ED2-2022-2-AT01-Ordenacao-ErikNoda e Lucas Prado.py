#Activity 01
#Lucas Prado & Erik Noda
#Data Structures 2

from ast import arg
import sys
import random
from time import time

#Heap Sort
def heapify(array, n, i,compare):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    compare += 1
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest,compare)
    return compare

def heapSort(array, compare):
    for i in range(len(array), -1, -1):
        compare = heapify(array, len(array), i, compare)
    for i in range(len(array)-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        compare = heapify(array, i, 0,compare)
    return compare

#Quick Sort
def quickSort(array, compare):
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
        quickSort(less, compare)
        quickSort(greater, compare)
        array[:] = less + [pivot] + greater
    return compare

#Merge Sort
def mergeSort(array, compare):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L, compare)
        mergeSort(M, compare)
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
def insertionSort(array, n, compare):
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
def selectionSort(array, n, compare):
    n -= 1
    for i in range(n):
        aux = i
        for j in range(i, n):
            if array[j] < array[aux]:
                aux = j
        compare += 1
        if aux != array[i]:
            array[aux], array[i] = array[i], array[aux]
    return compare

#Bubble Sort
def bubbleSort(array, n, compare):
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
if len(sys.argv)!=3:
    print("Quantidade de parametros invalida!")
    sys.exit()
sys.setrecursionlimit(100000)
#entrada = open('input1.txt','r')#abre arquivo para leitura
entrada = open(sys.argv[1],'r')
#saida = open('output1.txt','w')
saida = open(sys.argv[2],'w')

linha = entrada.readlines()
if '1' in linha[0] or '2' in linha[0] or '3' in linha[0] or '4' in linha[0] or '5' in linha[0] or '6' in linha[0] or '7' in linha[0] or '8' in linha[0] or '9' in linha[0]:
    condicao=1
else:
    saida.write("Arquivo Invalido")
    entrada.close()
    saida.close()
    sys.exit()

N = int(linha[0]) #tamanho do vetor
array = list(range(N))

if 'c' in linha[1]:
    for i in range(N):
        array[i] = i + 1
    #print(array)
elif 'd' in linha[1]:
    #d
    aux = N
    for i in range(N):
        array[i] = aux
        aux -=1
    #print(array)
elif 'r' in linha[1]:
    #random
    for i in range(N):
        array[i] = random.randint(0, 32000)
    #print(array)
else:
    print('Entrada de arquivo invalido! Não especificado tipo C, D ou R')
    sys.exit()

#sorts
saida.write("vetor desordenado: ")
for i in range(N):
    saida.write("%d " % array[i])

for i in range (6):
    comp = 0
    if i == 0:
        start = time()
        comp = insertionSort(array, len(array), comp)
        end = time()
        tempo = (end-start)*1000
        saida.write("\ninsertionSort: ")
        for i in range (N):
            saida.write("%d " % array[i])
        saida.write(", %d comp" % comp)
        saida.write(", %.2f ms\n" % tempo)

    elif i == 1:
        start = time()
        comp = selectionSort(array, len(array), comp)
        end = time()
        tempo = (end-start)*1000
        saida.write("selectionSort: ")
        for i in range (N):
           saida.write("%d " % array[i])
        saida.write(", %d comp" % comp)
        saida.write(", %.2f ms\n" % tempo)

    elif i == 2:
        start = time()
        comp = bubbleSort(array, len(array), comp)
        end = time()
        tempo = (end-start)*1000
        saida.write("bubbleSort: ")
        for i in range (N):
           saida.write("%d " % array[i])
        saida.write(", %d comp" % comp)
        saida.write(", %.2f ms\n" % tempo)

    elif i == 3:
        start = time()
        comp = mergeSort(array, comp)
        end = time()
        tempo = (end-start)*1000
        saida.write("mergeSort: ")
        for i in range (N):
           saida.write("%d " % array[i])
        saida.write(", %d comp" % comp)
        saida.write(", %.2f ms\n" % tempo)
    
    elif i == 4:
        start = time()
        comp = quickSort(array, comp)
        end = time()
        tempo = (end-start)*1000
        saida.write("quickSort: ")
        for i in range (N):
            saida.write("%d " % array[i])
        saida.write(", %d comp" % comp)
        saida.write(", %.2f ms\n" % tempo)

    elif i == 5:
        start = time()
        comp = heapSort(array, comp)
        end = time()
        tempo = (end-start)*1000
        saida.write("heapSort: ")
        for i in range (N):
            saida.write("%d " % array[i])
        saida.write(", %d comp" % comp)
        saida.write(", %.2f ms\n" % tempo)

entrada.close()
saida.close()