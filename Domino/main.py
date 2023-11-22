matrix = [list(map(int, input().split())) for _ in range(7)]
parts = []

for i in range(7):
  for j in range(7):
    if matrix[i][j] == 1:
      if [i, j] not in parts and [j, i] not in parts:
        parts.append([i, j])

print(len(parts))