def solution(tickets, res):
    answer = tickets
    res.sort(key = lambda x: (x[0], -x[1]))

    for i in res:
        if i[1] < tickets:
            tickets -= i[1]

    return answer - tickets

tickets, res = 10, [[1,5],[1,1],[2,4],[2,5],[4,7]]
print(solution(tickets, res))