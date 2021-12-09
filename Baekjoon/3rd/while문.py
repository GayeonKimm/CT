# 10952 A+B-5
# while True:
#     a,b = map(int, input().split())
#     if a==0 and b==0:
#         break
#     print(a+b)

# 10951 A+B-4
# break 조건을 안줬는데.. try except 로 풀어야 하나
# 입력 개수에 제한이 없기 때문에 작성
# 두 수가 입력되지 않으면 반복문 종료하려구
# while True:
#     try:
#         a,b = map(int, input().split())
#         print(a+b)
#     except:
#         break


# 1110 더하기 사이클
n = int(input())
num = n
cnt =0

while True:
    a = num//10
    b = num % 10
    c =(a+b) %10
    num = (b*10) +c
    cnt+=1
    if num == n:
        break
print(cnt)

# 잘했당