'''
접미사 배열
1. 들어온 문자를 앞글자 하나씩 떼서 list에 저장
2. sort
'''
import sys
input = sys.stdin.readline

s = input().strip()
answer = []
for i in range(len(s)):
    answer.append(s[i:])
answer.sort()

# 이 방법도 있지롱 - 이게 더 빠름
print('\n'.join(answer))
# for i in answer:
#     print(i)