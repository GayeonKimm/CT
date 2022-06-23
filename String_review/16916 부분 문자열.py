'''
접두어 문자 처럼 주어진 문자p와 같은길이만큼 s문자열을 slicing 해서 확인하는 문제
s for문 정의할 때 range 조절 필요!
'''
import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()

chk = False
for i in range(len(s)- len(p) + 1):
    if s[i:i+len(p)] == p:
        chk = True
        break
if chk:
    print(1)
else:
    print(0)