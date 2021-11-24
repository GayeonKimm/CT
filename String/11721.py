# a = '0123456789'
# b = '안녕하세요안'
# c = '0123456789'
# c = list(c)
# print(c)
# print(a[0:3]) # 0 ~ 2
# print(a[1:5])  # 1 ~ 4
# print(a[0:])
# print(b[1:])
# print(type(a))
# print(type(c))
# print(c[0:3]) # 0 ~ 2



# 11721 끊어서 출력하기
A = input()
for i in range(0, len(A),10):
    print(A[i:i+10])


# 11719 그대로 출력
# while True:
#     try:
#         print('''%s''' % input())
#     except EOFError:
#         break