# 10953 , 로 나눠진 값 더하기
# n = int(input())
# for i in range(n):
#     A,B = map(int, input().split(','))
#     print(A+B)

# 1541 읽어버린 괄호
# 왜 최솟값을 만들기 위해 (-)기준인 이유
# (-) 한 것들을 더하면 (-)결과

A = input().split(sep ='-')
num = []
for i in A:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
    print(num)
result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)

# len()!!! WARNING