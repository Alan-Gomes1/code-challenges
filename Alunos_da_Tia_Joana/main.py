def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = len(array) // 2
    value = array[pivot]
    left = [i for i in array if i < value]
    middle = [i for i in array if i == value]
    right = [i for i in array if i > value]
    response = quicksort(left) + middle + quicksort(right)
    return response


students = []
number_of_students, winner = map(int, input().split())

for i in range(number_of_students):
    students.append(input())

answer = quicksort(students)
print(answer[winner-1])
