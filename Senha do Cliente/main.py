def digito(numero):
  valores = []
  contador1 = 0
  contador2 = 0
  posicao = 2

  valores = [senhas[numero[0]-1][0], senhas[numero[0]-1][1]] # -1 pq é indexado em 0
  for i in range(1, qtde_senhas):
    if valores[0] in senhas[numero[i]-1][posicao:posicao+2]:
      contador1 += 1
    if valores[1] in senhas[numero[i]-1][posicao:posicao+2]:
      contador2 += 1
    posicao += 2

  if contador1 > contador2:
    return valores[0]
  else:
    return valores[1]

def posicao(valor):
  letras = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
  return letras[valor]

def senha(entrada):
  valor = []
  for i in range(6):
    num = []
    for j in range(qtde_senhas):
      num.append(posicao(entrada[j][i]))
    
    valor.append(digito(num))
  return valor

teste = 1
while True:
  qtde_senhas = int(input())
  if qtde_senhas == 0:
    break
  entrada = []
  senhas = [[], [], [], [], []]

  for i in range(qtde_senhas):
    entrada.append(input().split())
    l = 0
    for j in range(5):
      for k in range(2):
        senhas[j].append(int(entrada[i][l]))
        l += 1

  entrada = [valor[10:] for valor in entrada]
  senha_cliente = senha(entrada)
  print(f"Teste {teste}")
  for numero in senha_cliente:
    print(end=f"{numero} ")
  print("\n")
  teste += 1