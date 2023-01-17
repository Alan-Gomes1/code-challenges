letra = input()
texto = input()

palavras = 1.0
contador = 0.0
ocorrencia = False
quantidade = 0.0

for i, palavra in enumerate(texto):
  if letra == texto[i] and ocorrencia == False:
    contador += 1
    ocorrencia = True
  
  elif texto[i] == " ":
    palavras += 1
    ocorrencia = False


if palavras > 1 and contador > 0:
  quantidade = (contador / palavras) * 100
elif palavras == 1 and contador > 0:
  quantidade = 100.0
else:
  quantidade = 0.0

print(f'{quantidade:.1f}\n')