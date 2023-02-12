try:
  def validation(portion1, portion2, number):
    password = portion1 + portion2
    verification = False
    if password == number:
      verification = True
    elif str(portion1)[-1] == '0': # Remove os zeros da primeira parcela
      aux = str(portion1)[:-1]
      if aux[-1] == '0':
        aux = aux[:-1]
      portion1 = int(aux)
      password = portion1 + portion2
      if password == number:
        verification = True
      else:
        verification = False
    return print(f"{number}: S") if verification else print(f"{number}: N")


  while number := int(input()):
    if number == 1:
      print(f"{number}: S")
      continue
    potency = pow(number, 2)
    if len(str(potency)) == 1: # se houver apenas uma casa decimal não há como somar suas partes
      print(f"{number}: N")
      continue
    size = len(str(potency)) // 2
    portion1 = int(str(potency)[:size])
    portion2 = int(str(potency)[size:])
    if portion2 > 0: # a soma tem que ser entre números inteiros positivos
      validation(portion1, portion2, number)
    else:
      print(f"{number}: N")

except:
  pass