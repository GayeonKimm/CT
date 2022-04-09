import sys
input = sys.stdin.readline
n, m = map(int, input().split(':'))

# 최대공약수 구하는 함수
def gcd(n,m):
    a, b = max(n,m), min(n,m)
    while True:
        mod = a % b
        if mod == 0:
            return b
        else:
            a, b = b, mod
b = gcd(n,m)
print('%d:%d' %(n//b, m//b))

# def gcd(a, b):
#     while b > 0:
#         tmp = a
#         a = b
#         b = tmp % b
#     return a
