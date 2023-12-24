def quicksort(array, posicao):
    if len(array) <= 1:
        return array
    valor = array[len(array)//2][posicao]
    esquerda = [i for i in array if i[posicao] < valor]
    meio = [i for i in array if i[posicao] == valor]
    direita = [i for i in array if i[posicao] > valor]
    return quicksort(esquerda, posicao) + meio + quicksort(direita, posicao)

teste = 1
while S := int(input()):
    coordenadas = [list(map(int, input().split())) for _ in range(S)]
    meio = len(coordenadas) // 2
    pos_x = quicksort(coordenadas, 0)
    pos_y = quicksort(coordenadas, 1)
    print(f'Teste', teste)
    print(f'{pos_x[meio][0]} {pos_y[meio][1]}\n')
    teste += 1