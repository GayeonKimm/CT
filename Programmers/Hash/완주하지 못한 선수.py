def solution(participant, completion):
    d = dic()
    for p in participant:
        d[p] +=1
    for c in completion:
        d[c] -=1
        if d[c] == 0:
            d.pop(c)

    return




p =["leo", "kiki", "eden"]
c= ["eden", "kiki"]
print(solution(p, c))