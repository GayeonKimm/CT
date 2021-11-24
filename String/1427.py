# 1427 소트인사이드
# A = input()
# print(sorted(A))
# WRONG

# A = input()
# a = sorted(A)
# for i in a:
#     print(i,end='')
# WRONG- 문제를 잘못 읽음. 내림차순 정렬

A = input()
a = sorted(A)
for i in list(reversed(a)):
    print(i,end='')

# reversed() is not list def. =>list(reversed(a))