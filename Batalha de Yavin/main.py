N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
teleports = [list(map(int, input().split())) for _ in range(M)]
destroyed = 0

for row, col in teleports:
  for i in range(row - 1, -1, -1):
    if space[i][col] == 1:
      destroyed += 1
      space[i][col] = 0
      break

print(destroyed)