import math
registro, distanciaMax = map(int, input().split())
x = y = raiz = 0.0
afastou = False

for i in range (registro):
  direcao, distancia = input().split()
  if direcao == "N":
    y += int(distancia)
  elif direcao == "S":
    y -= int(distancia)
  elif direcao == "L":
    x += int(distancia)
  elif direcao == "O":
    x -= int(distancia)

  raiz = math.sqrt((x * x) + (y * y))
  if raiz > distanciaMax:
    afastou = True

print(1 if afastou else 0)