# 10610 30
# A = list(input())
# A = sorted(A, reverse=True)
# # A.sort(reverse=True)
# # print(A)
# sum = 0
# for i in A:
#     sum += int(i)
#
# if sum % 3 != 0 and '0' not in A:
#     print('-1')
# else:
#     print(''.join(A))

# ERROR CODE : 출력 초과

A = input()
A = sorted(A, reverse=True)
sum = 0
if '0' not in A:
    print(-1)
    # 제외할 건 제외하고 시작

else:
    for i in A:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(A))