# 1316 그룹단어 체커
# n = int(input())
# for _ in range(n):
#     A = input()
#     no_group = 0
#     for j in range(len(A)-1):
#         if A[j] == A[j+1]:
#             pass
#         elif A[j] == A[j+1:]:
#             no_group += 1
# print(n-no_group)
#
    # 뭐가 틀렸는지 확인

n = int(input())
no_group = 0
for _ in range(n):
    A = input()
    for j in range(len(A)-1):
        if A[j] == A[j+1]:
            pass
        elif A[j] in A[j+1:]:
            no_group += 1
            break
print(n-no_group)

# no_group의 위치와 print()의 위치 확인.