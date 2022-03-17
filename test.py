def solution(n, cnt, answer):
    if len(str(n)) > 1:
        cnt += 1
        t = 0
        for i in str(n):
            t += int(i)
        answer.append(t)
        solution(t, cnt, answer)

    else:
        return cnt, answer


## 왜 cnt가 반영이 안되는거지?????????

n = 753257
cnt = 0
answer = []
print(solution(n, cnt, answer))