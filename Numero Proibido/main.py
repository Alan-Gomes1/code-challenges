qtde = int(input())
numeros_proibidos = [int(numero) for numero in input().split()]
numeros_proibidos = sorted(set(numeros_proibidos))
try:
  while True:
    numero = int(input())
    if numero in numeros_proibidos:
      print("sim")
    else:
      print("nao")
except EOFError:
  pass