# level 2

def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for b in range(1, total+1):
        if (total/b) % 1 == 0:
            a = int(total/b)
            if a >= b:
                if 2*a + 2*b == brown +4:
                    return [a,b]
    return answer

brown, yellow = 10,2
print(solution(brown, yellow))