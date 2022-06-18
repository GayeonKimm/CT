'''
try - except 구문 사용!!

'''
import sys
input = sys.stdin.readline
from collections import Counter

answer = []
while True:
    try:
        n = input().strip()
        answer.append(n)
    except EOFError:
        break

result = sorted(answer)
for i in result:
    print(i, len(answer))
