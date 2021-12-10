def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant.pop()

# def solution(participant, completion):
#     d = dict()
#     for p in participant:
#         d[p] = d.get(p,0) + 1
#     for c in completion:
#         d[c] -= 1
#     answer = ''.join(k for k,v in d.items() if v>0)
#     return answer


p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]
print(solution(p, c))

# 1. name sorted
# 2. check. using zip(,)