def cima(linha, coluna, matriz):
    qtde = 0
    if 0 <= linha - 1 and matriz[linha-1][coluna] == 2:
        return 1
    elif matriz[linha-1][coluna] == 1:
        return 0
    qtde = cima(linha-1, coluna, matriz)
    return qtde


def baixo(linha, coluna, matriz):
    qtde = 0
    if linha + 1 < 8 and matriz[linha+1][coluna] == 2:
        return 1
    elif matriz[linha+1][coluna] == 1:
        return 0
    qtde = baixo(linha+1, coluna, matriz)
    return qtde


def direita(linha, coluna, matriz):
    qtde = 0
    if coluna + 1 < 8 and matriz[linha][coluna+1] == 2:
        return 1
    elif matriz[linha][coluna+1] == 1:
        return 0
    qtde = direita(linha, coluna+1, matriz)
    return qtde


def esquerda(linha, coluna, matriz):
    qtde = 0
    if 0 <= coluna - 1 and matriz[linha][coluna-1] == 2:
        return 1
    elif matriz[linha][coluna-1] == 1:
        return 0
    qtde = esquerda(linha, coluna-1, matriz)
    return qtde


tabuleiro = [list(map(int, input().split())) for _ in range(8)]
X, Y = map(int, input().split())
peças_inimigas = cima(X, Y, tabuleiro) + baixo(X, Y, tabuleiro) + direita(X, Y, tabuleiro) + esquerda(X, Y, tabuleiro)
print(peças_inimigas)
