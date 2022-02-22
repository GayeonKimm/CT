# 특정 기준으로 나눈수들 끼리 더해나가서 마지막 한자리가 될 때 몇번 나ㅇ눴는지 출력
# 마지막 한자리수는 뭐가 나오든 상관없음

def solution(n):
    if len(str(n)) == 1:
        return n
    else:
        t = 0
        for i in str(n):
            t += int(i)
        solution(t)

    return




n = 753257
print(solution(n))