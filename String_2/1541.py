# 잃어버린 괄호
# 그리디

# import sys
# imput = sys.stdin.readline

# 풀었던 방식이랑은 다르게
s = input().split("-")

sum = 0
for i in s[0].split("+"):
    sum += int(i)
# 첫번째 숫자는 고이 접어 저장

# 그 뒤부터는 계속 숫자를 뺌
for i in s[1:]:
    for j in i.split("+"):
        sum -= int(j)
print(sum)


