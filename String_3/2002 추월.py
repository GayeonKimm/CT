import sys
input = sys.stdin.readline
'''
추월을 했다는 걸 어떻게 잡아내지? 
= 번호를 부여하자
누구에게? = enter한 차 들에게

- 몇 대를 추월했느냐가 아니라 몇 대의 차가 추월을 했냐
'''
n = int(input())
answer = 0
en = {}
for i in range(n):
    en[input().strip()] = i
ex = [input().strip() for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if en[ex[i]] > en[ex[j]]:
            answer += 1
            break # 하나라도 있으면 다음 out 순서로 넘어가도 됨
print(answer)