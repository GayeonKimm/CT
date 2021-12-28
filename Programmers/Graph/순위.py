#level3

from collections import defaultdict

def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)

    for winner, loser in results:
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)


    for i in range(1, n+1):
        for winner in win_graph[i]:
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:
            win_graph[loser].update(win_graph[i])


    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))