# 최대공약수와 최소공배수
# 유클리드 호제법
def gcd(n, m):
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(n, m)
    else:   # mod == 0이면 작은 수가 최대공약수가 되니깐
        return n

def solution(n, m):
    return [gcd(n, m), int(m*n/gcd(n, m))]


# n,m = 3,12
n,m = 2,5
print(solution(n,m))