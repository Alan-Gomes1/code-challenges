qtde_carcacteres, qtde_minusculas, qtde_maiusculas, qtde_numeros = map(int, input().split())
senha = input()
minuscula = maiuscula = numero = 0

for i in range (len(senha)):
  if senha[i] >= "A" and senha[i] <= "Z": #[A-Z]
    maiuscula += 1
  elif senha[i] >= "a" and senha[i] <= "z": #[a-z]
    minuscula += 1
  elif senha[i] >= "0" and senha[i] <= "9": # [0-9]
    numero += 1

print("Ok =/" if qtde_carcacteres <= len(senha) and maiuscula >= qtde_maiusculas 
and minuscula >= qtde_minusculas and numero >= qtde_numeros else "Ufa :)")