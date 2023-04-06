abertura = int(input())
qtde_estrelas = int(input())
perceptivel = 0

for i in range (qtde_estrelas):
  estrelas = 0
  estrelas = int(input())
  if abertura * estrelas >= 40000000:
    perceptivel += 1

print(perceptivel)