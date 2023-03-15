def MissingDigit(strParam):
  parcela1, sinal, parcela2, igual, resultado = strParam.split()
  if strParam.index("x") < strParam.index("="):
    for i in range(10):
      equacao = strParam.replace("x", str(i))[:strParam.index(igual)]
      if int(eval(equacao)) == int(resultado):
        return i
  else:
    for i in range(10):
      equacao = resultado.replace("x", str(i))
      if int(eval(strParam[:strParam.index(igual)])) == int(eval(equacao)):
        return i
    

print(MissingDigit(input()))