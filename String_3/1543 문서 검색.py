'''
주어진 문자를 한글자씩 확인하고 다 맞으면 다시 문자 새로 돌아
'''
import sys
input = sys.stdin.readline

ans = input().strip()
t = input().strip()

answer = 0
n = 0
while n <= len(ans)-len(t):
    if ans[n:n+len(t)] == t:
        answer += 1
        n += len(t)
    else:
        n += 1
print(answer)