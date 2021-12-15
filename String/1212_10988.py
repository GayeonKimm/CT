# 1212 8진수로 들어온거 2진수로 바꾸기
# A = int(input(),8)
# print(bin(A)[2:])

# 10988 팰린드롬인지 확인하기
A = input()
if A == A[::-1]:
    print(1)
else:
    print(0)