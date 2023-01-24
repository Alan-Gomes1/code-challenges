def rumo_aos9(entrada, grau):
  if len(str(entrada)) == 1:
    if entrada % 9 == 0:
      if grau == 0:
        return 1
      else:
        return grau
    else:
      return 0
  else:
    grau += 1
    soma = str(entrada)
    entrada = 0
    for i in range(len(soma)):
      entrada += int(soma[i])

    return rumo_aos9(entrada, grau)

while True:
  grau = 0
  entrada = int(input())
  if entrada == 0:
    break

  degree = rumo_aos9(entrada, grau)
  if degree != 0:
    print(f"{entrada} is a multiple of 9 and has 9-degree {degree}.")
  else:
    print(f"{entrada} is not a multiple of 9.")