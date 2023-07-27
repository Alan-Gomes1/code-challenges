tempo = int(input())
horas = int(tempo / 3600)
tempo_restante = int(tempo - (horas * 3600))
minutos = int(tempo_restante / 60)
segundos = int(tempo_restante % 60)

print(f'{horas}h {minutos}m {segundos}s')
