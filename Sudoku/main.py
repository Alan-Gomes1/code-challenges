def solucao_sudoku(matriz):
    def verifica_linhas_colunas(matriz):
        for i in range(9):
            linhas = [matriz[i][j] for j in range(9)]
            colunas = [matriz[j][i] for j in range(9)]
            if len(set(linhas)) != 9 or len(set(colunas)) != 9:
                return False
        return True

    def verifica_regioes(matriz):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                regiao = [matriz[x][j: j+3] for x in range(i, i+3)]
                if len(set(regiao[0] + regiao[1] + regiao[2])) != 9:
                    return False
        return True

    return verifica_linhas_colunas(matriz) and verifica_regioes(matriz)


n = int(input())
for instancia in range(1, n + 1):
    matriz = [list(map(int, input().split())) for _ in range(9)]
    resposta = 'SIM' if solucao_sudoku(matriz) else 'NAO'
    print(f'Instancia {instancia}')
    print(resposta)
    print()
