amount_cars, turns = [int(value) for value in input().split()]
cars = [0 for i in range(amount_cars)]

for i in range(amount_cars):
  time = 0
  round = [int(value) for value in input().split()]
  for value in (round):
    time += value
  cars[i] += (time)

winners = sorted(cars)[:3]
for i in range(3):
  print(cars.index(winners[i])+1)