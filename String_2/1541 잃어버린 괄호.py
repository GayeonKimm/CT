# 재풀이 완
# 그리디
import sys
imput = sys.stdin.readline

# 최소값 만들거니까 -로 분리
s = input().strip().split("-")

sum = 0
for i in s[0].split("+"):
    sum += int(i)
# 첫번째 분리된 것은 더해서 저장
# 그 뒤부터는 계속 숫자를 뺌
# 마이너스 분배
for i in s[1:]:
    for j in i.split("+"):
        sum -= int(j)
print(sum)

