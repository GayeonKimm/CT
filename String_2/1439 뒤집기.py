'''
11111000110100001 -> 1010101 로 바꾸는것이 핵심
1. cnt -> for문으로 비교하기
2. split 하고 count세기
'''
import sys
input = sys.stdin.readline

s = input().strip()
cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1
print((cnt+1)//2)

# 요렇게도 가능하구... 메모리 시간 둘 다 큰 차이 없음
import sys
input = sys.stdin.readline
s1 = input().strip()
b = s1.split("0")
c = s1.split("1")

b2 = b.count('') # 공백은 아웃
c2 = c.count('')
print(min(len(b)-b2, len(c)-c2))