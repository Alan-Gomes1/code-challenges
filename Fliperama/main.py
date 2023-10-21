def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = int(len(array)/2)
    value = array[pivot]
    left = [i for i in array if i < value]
    middle = [i for i in array if i == value]
    right = [i for i in array if i > value]

    response = quicksort(right) + middle + quicksort(left)
    return response


punctuation = []
rounds, scoreboard = input().split()
for i in range(int(rounds)):
    punctuation.append(int(input()))
    print(*quicksort(punctuation)[:int(scoreboard)], sep='\n')
