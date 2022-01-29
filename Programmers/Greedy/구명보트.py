# level 2
def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people)-1
    while i <= j:
        answer += 1
        if people[i]+people[j] <= limit:
            i += 1
        j -= 1
    return answer

# people = [70,50,80,50]
people = [40,50,50,50,70,80,90]
limit = 100
print(solution(people, limit))