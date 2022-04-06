def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    print('*')
    return participant.pop()
    # return participant[-1] #도 가능


p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]
print(solution(p, c))

# 1. name sorted
# 2. check. using zip(,)