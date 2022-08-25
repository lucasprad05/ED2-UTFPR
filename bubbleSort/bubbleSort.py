#Bubble Sort
#Lucas Prado & Erik Noda
#Data Structures 2

def bubbleSort(v, o):
    change = True
    n = len(v)

    while change == True:
        change = False
        for i in range(n - 1):
            if o == '0':#crescente
                if v[i] > v[i + 1]:
                    v[i], v[i + 1] = v[i + 1], v[i]
                    change = True
                    print(v)
            else:#decrescente
                if v[i] < v[i + 1]:
                    v[i], v[i + 1] = v[i + 1], v[i]
                    change = True
                    print(v)

o = input('Escolha a opção para escrever:\n 0 - Crescente\n 1 - Descrescente\n')
v = [-19, -61, -36, 36, -48, 32, -9, 16, -34, -77, 80, -26, -18, -27, 84]
bubbleSort(v, o)
