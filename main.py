mensagem = input()
contador = 0

for i in range (len(mensagem)):
  if contador % 2 != 0: # retorna todos os caracteres na posição ímpar
    print(end=mensagem[i])
  contador += 1

  if mensagem[i] == " ":
    print(end=" ")
    contador = 0 # reinicia o contador para verificar outra palavra após o espaço