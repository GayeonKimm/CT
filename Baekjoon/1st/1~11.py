# 2557. 지겨운 Hello World! 출력
# print("Hello World!")

# 10718. 강한친구 대한육군을 한 줄에 한 번씩 출력
# print("강한친구 대한육군\n강한친구 대한육군")
# print("강한친구 대한육군\n"*2)

# 10171 고양이.. 인건지 모르겠는
# print('''
# \    /\
#  )  ( ')
# (  /  )
#  \(__)| ''')

#10172 개 출력
# print('''
# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|
# ''')

# # 1000. A+B
# a, b = map(int, input().split())
# print(a+b)
#
# # 1001 A-B
# a, b = map(int, input().split())
# print(a-b)
#
# # 10998 AxB
# a, b = map(int, input().split())
# print(a*b)
#
# # 1008 A/B
# a, b = map(int, input().split())
# print(a/b)

# 10869 사칙연산
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# 10430. 나머지
# A,B,C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

# 2588 곱셈. 세자리수x세자리수 =?
num1 = int(input())
num2 = int(input())
print(num1*(num2%10))             # %10은 일의자리수만 뽑아서
print(num1*((num2%100)//10))      # %100)//10 십의 자리수만 뽑기
print(num1*((num2%1000)//100))
print(num1*num2)


