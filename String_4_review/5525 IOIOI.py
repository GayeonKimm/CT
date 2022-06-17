import sys
input = sys.stdin.readline

n = int(input())
m = int(input()) # s 길이
s = input().strip()
answer = 0

p = 'I' + 'OI' * n
for i in range(len(s) - len(p) + 1):
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        if s[i:i+len(p)] == p:
            answer += 1
print(answer)