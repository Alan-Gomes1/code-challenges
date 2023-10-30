test_number = 1
while True:
    n = int(input())
    if n == 0:
        break

    goals = []
    best_period = (1, 1)
    max_goal_diff = 0
    current_diff = 0
    period_start = 1

    for i in range(n):
        goals_for, goals_against = map(int, input().split())
        diff = goals_for - goals_against
        current_diff += diff

        if current_diff > max_goal_diff:
            max_goal_diff = current_diff
            best_period = (period_start, i + 1)
        elif current_diff == max_goal_diff and (i + 1 - period_start) > (best_period[1] - best_period[0]):
            best_period = (period_start, i + 1)

        if current_diff < 0:
            current_diff = 0
            period_start = i + 2

    print("Teste", test_number)
    if max_goal_diff <= 0:
        print("nenhum")
    else:
        print(best_period[0], best_period[1])
    print()

    test_number += 1
