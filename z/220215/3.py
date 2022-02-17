"""
a = 3000원
b = 5000원
현재 있는 돈은 23000원
경우의 수를 따져서 현재 돈에 딱 맞게 각각 몇 개를 살 수 있는지

예전에 풀어본 문제 같은데 몇번인지 기억이 안나
"""

def solution(a,b,now):
    answer = 0
    temp = now//b
    for y in range(1, temp+1):
        x = (now-b*y)/a
        if x % 1 == 0:
            answer += 1
    return answer



a,b, now = 3000,5000,23000
print(solution(a,b,now))