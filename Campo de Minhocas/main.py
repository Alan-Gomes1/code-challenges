linhas, colunas = map(int, input().split())
fazenda = [[] for i in range(linhas)]
minhocas = 0

for i in range (linhas): # Preenche o vetor e calcula a maior qtde nas colunas
  soma = 0
  fazenda[i] = [int(valor) for valor in input().split()]
  for valor in fazenda[i]:
    soma += valor
  if soma > minhocas:
    minhocas = soma

for i in range (colunas): # Calcula a maior qtde nas linhas
  soma = 0
  for j in range (linhas):
    soma += fazenda[j][i]
  if soma > minhocas:
    minhocas = soma

print(minhocas)