# 1769 3의 배수 문제 참고

def solution(n, cnt, answer):
    while len(str(n)) > 1 :
        cnt += 1
        hap = 0
        for i in str(n):
            hap += int(i)
        n = str(hap)
        answer.append(n)

    else:
        return cnt, answer


n = 753257
cnt = 0
answer = []
print(solution(n, cnt, answer))