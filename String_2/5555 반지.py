# 프로그래머스 괄호 회전하기 문제랑 똑같은디

import sys
input = sys.stdin.readline

# s = input().strip()
# n = int(input())
# answer = 0
# for _ in range(n):
#     ring = input().strip()
#     temp = ring
#     for i in range(len(ring)):
#         temp = temp[1:] + temp[0]
#         if s in temp:
#             answer += 1
#             break
# print(answer)

# 다른 방법도 있지! - 걍 2배하는 법이여

s = input().strip()
answer = 0
for _ in range(int(input())):
    ring = input().strip()
    if s in ring*2:
        answer += 1
print(answer)