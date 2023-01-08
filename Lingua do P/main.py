message = input()
counter = 0

for i in range (len(message)):
  if counter % 2 != 0: # retorna todos os caracteres na posição ímpar
    print(end=message[i])
  counter += 1

  if message[i] == " ":
    print(end=" ")
    counter = 0 # reinicia o counter para verificar outra palavra após o espaço
    