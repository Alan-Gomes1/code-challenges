dimensao = int(input())

amazonia = [list(map(int, input().split())) for _ in range(dimensao)]
qtde_coordenadas = int(input())
especies = 0

for i in range(qtde_coordenadas):
    x, y = map(int, input().split())
    especies += amazonia[x][y]

print(especies)