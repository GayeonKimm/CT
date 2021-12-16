"""
1. 아이디어
- 백트래킹 재귀함수 안에서, for문 돌면서 숫자 선택(이때 방문여부 확인)
- 재귀함수에서 M개를 선택할 경우 print

2. 시간복잡도
- N! 인경우라 N= 8 << 10까지니까 가능.

3. 자료구조
- 결과값 저장 int []
- 방문여부 bool[]
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False]*(N+1)
print(chk)
# 접근 편하게 하려고

def recur(num):
    if num == M:
        print(" ".join(map(str, rs)))
        return

    for i in range(1, N+1):
        # 방문여부 확인
        if chk[i] == False:
            chk[i] = True

            rs.append(i)
            recur(num+1)

            chk[i] = False
            rs.pop()

recur(0)  # 0부터 시작



