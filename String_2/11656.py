# 11656 접미사 배열
import sys
input = sys.stdin.readline

s = input().strip()
answer = []
for i in range(len(s)):
    answer.append(s[i:])
    # answer += s[i:]
print(answer)
answer.sort()
for i in answer:
    print(i)




