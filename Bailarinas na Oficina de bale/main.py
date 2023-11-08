n = int(input())
bailarinas = list(map(int, input().split()))
posicoes = [(i, bailarina) for i, bailarina in enumerate(bailarinas)]
posicoes = sorted(posicoes, key=lambda x: x[1])
pares = 0

for i in range(n-1):
    for j in range(i+1, n):
        if posicoes[i][0] > posicoes[j][0] and posicoes[i][1] <= posicoes[j][1]:
            pares += 1

print(pares)
