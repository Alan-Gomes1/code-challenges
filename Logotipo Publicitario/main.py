def aparece(logotipo, matriz):
    x, y = len(logotipo), len(logotipo[0])
    m, n = len(matriz), len(matriz[0])
    contador = 0
    for i in range(m - x + 1):
        for j in range(n - y + 1):
            corresponde = True
            for k in range(x):
                if matriz[i + k][j:j + y] != logotipo[k]:
                    corresponde = False
                    break
            if corresponde:
                contador += 1
    return contador

identificador = 1
x, y = map(int, input().split())


while x and y:
    logotipo = [list(map(int, input().split())) for _ in range(x)]
    k, m, n = map(int, input().split())
    contador = 0
    for _ in range(k):
        matriz = [list(map(int, input().split())) for _ in range(m)]
        contador += aparece(logotipo, matriz)
    
    print(f'Logotipo {identificador}')
    print(contador)
    print()
    identificador += 1
    x, y = map(int, input().split())
