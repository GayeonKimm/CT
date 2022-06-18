'''
수 n,m
첫줄에 dna
다른 것의 개수가 hamming distance를 다 더해서 출력
사전순으로 가장 앞서는 것 출력
'''
import sys
input =sys.stdin.readline

n,m = map(int, input().split())
chk = [[i for i in input().strip()] for _ in range(n)]
# [['Z', 'X', 'C', 'V', 'B'],
# ['Z', 'X', 'X', 'V', 'B'],
# ['Z', 'C', 'C', 'V', 'B'],
# ['Z', 'X', 'C', 'V', 'B'],
# ['A', 'S', 'D', 'F', 'G']]
print(chk)
'''
s = []
for i in range(n):
    s.append(list(input().strip()))
'''

answer = ''
cnt = 0
for j in range(m):
    a, c, t, g = 0, 0, 0, 0
    for i in range(n):
        if chk[i][j] == 'A':
            a += 1
        elif chk[i][j] == 'C':
            c += 1
        elif chk[i][j] == 'G':
            g += 1
        elif chk[i][j] == 'T':
            t += 1

    # 다 돌고나서
    if max(a,c,t,g) == a:
        answer += 'A'
        cnt += c+t+g
    elif max(a,c,t,g) == c:
        answer += 'C'
        cnt += a+t+g
    elif max(a,c,t,g) == g:
        answer += 'G'
        cnt += a+c+t
    elif max(a,c,t,g) == t:
        answer += 'T'
        cnt += a+c+g

print(answer)
print(cnt)