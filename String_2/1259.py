# 1259번 팰린드롬수
# while True:
#     A = list(input())
#     B = A[::-1]
#
#     if A == 0:
#         break
#
#     for i in range(len(A)):
#         if A[i] == B[i]:
#             print('yes')
#         else:
#             print('no')
# ERORR CODE

while True:
    A = input()
    if A == '0':
        break
    if A == A[::-1]:
        print('yes')
    else:
        print('no')
# for문으로 하나씩 비교 말고 그냥 한번에 확인 하는 방식으로 sol