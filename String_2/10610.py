# 10610 30의 배수 찾기

import sys
input = sys.stdin.readline

k = list(input().strip())
k.sort(reverse=True)
sum = 0
for i in k:
    sum += int(i)

if sum % 3 == 0:
    if k[-1] == '0':
        print("".join(k))
    else:
        print('-1')

else:
    print('-1')

# 이렇게 했을 때 k[-1] == '0' (0-> '0')으로 변경해야 돌아감
# k 를 list로 받았을 때, 숫자로 받느냐 문자로 받느냐에 따라 달라짐
# 문자로 받았기 때문에 sum을 문자씩 돌려가면서 더해야 하고
# 문자로 받았기 때문에 0이 있냐고 물어볼때도 '0'이라고 표시해야됨
# print join을 할때도 문자만 합쳐질 수 있나봄


# # k = list(map(int, input().strip()))
# k = list(input().strip())
# # 숫자가 아니라 문자로 입력을 받았어야 했네
# print(k)
# k.sort(reverse=True)
# sum = 0
# for i in k:
#     sum += int(i)
# if sum % 3 != 0 or "0" not in k:
#     print(-1)
#
# else:
#     print("".join(k))
