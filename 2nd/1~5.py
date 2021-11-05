# 기초 여러번했던 거니까 빠르게 빠르게

# 1330. 두 수 비교하기
# a,b = map(int, input().split())
# if a>b :
#     print(">")
# elif a==b:
#     print("==")
# else :
#     print("<")

# 9498. 시험 성적
# grade = int(input())
# if 90 <= grade <= 100:
#     print("A")
# elif 80 <= grade <= 89:
#     print("B")
# elif 70 <= grade <= 79:
#     print("C")
# elif 60 <= grade <= 69:
#     print("D")
# else :
#     print("F")

# 2753. 윤년
# month = int(input())
#
# if month%4 == 0 and month%100 != 0:
#     print('1')
# elif month%400 == 0:       # 4의 배수이면서 400의 배수니까 400의 배수이기만 하면 됨
#     print('1')
# else:
#     print('0')

# 14681 사분면 고르기
# x = int(input())
# y = int(input())
# if x>0 and y>0:
#     print('1')
# elif x<0 and y>0:
#     print('2')
# elif x<0 and y<0:
#     print('3')
# elif x>0 and y<0:
#     print('4')

#2884 상근아 학교가자....
h, m = map(int, input().split())
if m >= 45:
    print(h, m-45)
elif m<45 and h>0:
    print(h-1, m+15)
else:
    print(23, m+15)

# 시계는 60분 간격이니까 45분 이상으로 설정하면 단순 계산
# 45 미만의 값이 주어지면 h 값도 줄어들고 m에 단순 계산
# h 가 0으로 주어지면 23으로 설정하기
# 쏘 이지
