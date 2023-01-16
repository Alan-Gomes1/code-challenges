def ordena(numeros):
  n = len(numeros)
  for i in range(n-1):
    maior = i
    for j in range(i+1, n):
      if numeros[j][1] >= numeros[maior][1] and numeros[j][0] < numeros[maior][0]:
        maior = j
      elif numeros[j][1] > numeros[maior][1]:
        maior = j
    if i != maior:
      numeros[i][0], numeros[maior][0] = numeros[maior][0], numeros[i][0]
      numeros[i][1], numeros[maior][1] = numeros[maior][1], numeros[i][1]
  return numeros

def pontuacao_maxima(soma):
  pontuacao = 0
  for valor in soma:
      pontuacao += valor
  return pontuacao

teste = 1
while (qtde_jogadores := int(input())):
  alunos = []
  alunos = [[] for i in range(qtde_jogadores)]

  for i in range(qtde_jogadores):
    soma = []
    pontuacao = 0
    alunos[i].append(input())
    soma = [int(valor) for valor in input().split()]
    soma = sorted(soma)
    soma.remove(soma[0])
    soma.remove(soma[-1])
    pontuacao = pontuacao_maxima(soma)
    alunos[i].append(pontuacao)

  alunos = ordena(alunos)
  posicao = []
  posicao = [i+1 for i in range(qtde_jogadores)]
  for i in range(1, len(alunos)):
    if alunos[i][1] == alunos[i-1][1]:
      posicao[i] = posicao[i-1]

  print(f"Teste {teste}")
  [print(posicao[i], alunos[i][1], alunos[i][0]) for i in range(qtde_jogadores)]
  print()
  teste += 1