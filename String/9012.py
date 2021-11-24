# 9012
# n = int(input())
# for i in range(n):
#     A = input()
#     A_list = list(set(A))
#     cnt = []
#     for j in A_list:
#         count = A.count(j)
#         cnt.append(count)
#     if cnt[0] == cnt[1]:
#         print("YES")
#     else:
#         print('NO')
# 런타임 오류, 아마 마지막 인덱스 지정한 거 때문에?


# n = int(input())
# for i in range(n):
#     A = list(input())
#     sum = 0
#     for j in A:
#         if j == '(':
#             sum +=1
#         else :
#             sum -=1
#     if sum == 0:
#         print("YES")
#     else:
#         print("NO")
# wrong

# '('가 먼저 들어온다고 고정해야 됨
# 괄호의 시작은 ( 이니까
n = int(input())
for i in range(n):
    A = list(input())
    sum = 0
    for j in A:
        if j == '(':
            sum +=1
        elif j ==')':
            sum -=1
        if sum < 0:
            print("NO")
            break

    if sum > 0:
        print("NO")
    elif sum ==0:
        print("YES")
