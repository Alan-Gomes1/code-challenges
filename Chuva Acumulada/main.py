dimensão = int(input())
chuvas = [[] for i in range(dimensão)]
acumulado = [[] for i in range(dimensão)]
for i in range(dimensão):
  chuvas[i] += map(int, input().split())

for j in range(dimensão):
  acumulado[j] += map(int, input().split())
  for k in range (dimensão):
    chuvas[j][k] += acumulado[j][k]
del acumulado
# substituindo os caracteres de lista por vazio
[print(str(chuva).replace(",", "").replace("[", "").replace("]", "")) for chuva in chuvas]