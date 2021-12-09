# 2739 구구단 이지 이지 허리업
# n = int(input())
# for i in range(1,10):
#     print(n,'*',i,'=',n*i)

# 10950. A+B-3
# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     print(a+b)

# 8393 합
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)

# 15552 빠른 A+B
'''
Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
단, 이때는 맨 끝의 개행 문자까지 같이 입력받기 때문에
문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
'''

# import sys
# t = int(sys.stdin.readline())
# for i in range(t):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)

# 2741. N 찍기
# n = int(input())
# for i in range(1,n+1):
#     print(i)

# method2 가 더 괜찮은거 같애 위에 거는 조금 일차원적인듯?
# n = int(input())
# for i in range(n):
#     print(i+1)

# 2742. 기찍 N
# n = int(input())
# for i in range(n,0,-1):
#     print(i)

# method2로
# n = int(input())
# for i in range(n):
#     print(n-i)

# 11021. A+B-7
# t = int(input())
# for i in range(t):
#     a,b = map(int, input().split())
#     print(f'Case#{i+1} : {a+b}')

# 11022. A+B-8
# t = int(input())
# for i in range(t):
#     a,b = map(int, input().split())
#     print(f'Case#{i+1} : {a}+{b}={a+b}')

# 2438 2439 별찍자 1학년이 된 기분
# s = int(input())
# for i in range(1,s+1):
#     print('*'* i)
#
# for i in range(1,s+1):
#     print(' ' *(s-i)+'*'*i)

# 10871 X보다 작은 수
n, x = map(int, input().split())
list = list(map(int, input().split()))
list2 =[]
for i in range(n):
    if list[i] < x:
        list2.append(list[i])
print(*list2)   # 숫자만 나와유
print(list2)    # 꺽쇠 같이 나오구
