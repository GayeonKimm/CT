# 11654 아스키코드
# print(ord(input()))

# 11720 숫자의 합
# n = int(input())
# s = list(map(int, input()))
# # print(s)
# sum = 0
# for i in s:
#     sum += i
# print(sum)

# 리스트로 안하는법
# s = int(input())
# sum = 0
# for i in str(s):
#     sum += i
# print(sum)

# 10809 알파벳 찾기
# from string import ascii_lowercase
# alpha_list = list(ascii_lowercase)
# 런타임 에러... 아스키 코드로 작성하래 빌드업 오진다 근데 누가 외우고 다녀
# alpha = list(range(97,123))

# s = list(input())
# alpha = list('abcdefghijklmnopqrstuvwxyz')
#
# for i in alpha:
#     if i in s:
#         print(s.index(i), end = ' ')
#     else :
#         print('-1', end = ' ')


# 2675 문자열 반복
t = int(input())
s_list=[]
for i in range(t):
    temp = input().split()
    s_list.append(temp)
# print(s_list)

for i in s_list:
    r = int(i[0])
    s = list(i[1])
    for j in s:
        print(j*r, end = '')
    print('/')