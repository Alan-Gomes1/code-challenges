test = 1
while matches := int(input()):
  player1 = input()
  player2 = input()
  print(f"Teste {test}")
  for i in range(matches):
    play1, play2 = map(int, input().split())
    if (play1 + play2) % 2 == 0:
      print(player1)
    else:
      print(player2)
  test += 1
