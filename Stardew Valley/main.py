
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
axis, position = input().split()
position = int(position) - 1
answer = j = 0

if axis == 'L':
    answer = sum(matrix[position])
else:
    answer = sum(row[position] for row in matrix)

print(answer, '\n')