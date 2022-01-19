# DNA
# 코드 똑같이 작성했는데 틀렸다고함 이게 말이 되나

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(input().strip()))
# s.append(list(map(int, input().strip())))

hap = 0
answer = ''
for i in range(m):
    a,c,g,t = 0,0,0,0

    for j in range(n):
        if s[j][i]=='T':
            t += 1
        elif s[j][i]=='A':
            a += 1
        elif s[j][i]=='G':
            g += 1
        elif s[j][i]=='C':
            c += 1
    if max(a,c,g,t) == a:
        answer += 'A'
        hap += c+g+t
    elif max(a,c,g,t) == c:
        answer += 'C'
        hap += a+g+t
    elif max(a,c,g,t) == g:
        answer += 'G'
        hap += c+a+t
    elif max(a,c,g,t) == t:
        answer += 'T'
        hap += c+g+a

print(answer)
print(hap)