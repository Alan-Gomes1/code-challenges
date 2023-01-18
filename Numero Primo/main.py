numero = int(input())
contagem = 0

for i in range(1, numero + 1):
  if numero % i == 0:
    contagem += 1

if contagem == 2:
  print("sim")
else:
  print("nao")