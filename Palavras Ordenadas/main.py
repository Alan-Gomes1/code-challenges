qtde = int(input())
resposta = 'O'

for i in range (qtde):
  palavra = input()
  texto = palavra.casefold()
  for j in range (len(texto) - 1):
    if texto[j] >= texto[j+1]:
      resposta = 'N'
      break
  print(f"{palavra}: {resposta}")
print ()