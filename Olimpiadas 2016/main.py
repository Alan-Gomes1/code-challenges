numero_paises, numero_modalidades = map(int, input().split())
medalhas = {i: 0 for i in range(1, numero_paises+1)}

for _ in range(numero_modalidades):
    O, P, B = map(int, input().split())
    medalhas[O] += 1
    medalhas[P] += 1
    medalhas[B] += 1

classificacao = sorted(medalhas.keys(), key=lambda x: -medalhas[x])
print(*classificacao)
