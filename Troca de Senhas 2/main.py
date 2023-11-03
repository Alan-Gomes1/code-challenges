class TrocaSenha:
    def __init__(self, linha):
        self._matriz = []
        self.tamanho = len(linha)
        self.preenche_matriz(linha)

    def preenche_matriz(self, linha):
        self._matriz.append(linha)
        for i in range(self.tamanho-1):
            self._matriz.append(list(map(int, input().split())))
        self.descriptografa()

    def elimina_linha(self):
        diagonal = j = 0
        tamanho = len(self._matriz[0])
        for i in range(tamanho):
            diagonal += self._matriz[i][j]
            j += 1
        return int(diagonal % tamanho)

    def eliminha_coluna(self):
        diagonal = j = 0
        tamanho = len(self._matriz[0])
        for i in range(tamanho - 1, -1, -1):
            diagonal += self._matriz[j][i]
            j += 1
        return int(diagonal % tamanho)

    def descriptografa(self):
        while len(self._matriz) > 1:
            x = self.elimina_linha()
            y = self.eliminha_coluna()
            del self._matriz[x]
            for i in range(len(self._matriz)):
                self._matriz[i].pop(y)

    def __str__(self):
        senha = self._matriz[0][0]
        return str(senha)


linha = list(map(int, input().split()))
senha = TrocaSenha(linha)
print(senha)
