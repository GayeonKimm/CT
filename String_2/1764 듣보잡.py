# 1764 듣보잡
# 재풀이

import sys
input = sys.stdin.readline

N_list = set()
M_list = set()
N, M = map(int, input().split())
for _ in range(N):
    N_list.add(input().strip())
for _ in range(M):
    M_list.add(input().strip())


answer = sorted(list(N_list & M_list))
print(len(answer))
print("\n".join(answer))

'''
'str' object cannot be interpreted as an integer 오류 원인
- n, m split()할 때 int처리 안해서 그럼
'''

# 시간초과 코드
n, m = map(int, input().split())
listen = [input().strip() for _ in range(n)]
see = [input().strip() for _ in range(m)]
answer = []
for i in listen:
    if i in see:
        answer.append(i)
answer.sort()
print(len(answer))
for i in answer:
    print(i)