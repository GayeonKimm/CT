'''
숫자를 문자로 받아들이는데
다 달라야 하는 경우의 수 출력

123456 -> 6글자
뒤에서 3글자로 구별이 가능하면 break
그렇지 않으면 nums = k가 같아질 때겠지

'''
import sys
input = sys.stdin.readline

n = int(input())
numbers = [input().strip() for _ in range(n)]
num = len(numbers[0])

chk = False
k = 1
# 글자수와 k가 같아질 때까지
while k < num:
    temp = set()
    for i in numbers:
        temp.add(i[-k:])
    # 구별이 가능하다면
    if len(temp) == n:
        chk = True
        break
    k += 1

if chk:
    print(k)
else:
    print(num)

