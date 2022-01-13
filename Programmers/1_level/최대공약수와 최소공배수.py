# 최대공약수와 최소공배수

# gcd 사용하지 않는 방법
# def solution(n, m):
#     # n = min(n,m)
#     # m = max(n,m)
#     # 이거 자체만으로도 시간이 많이 걸림
#     answer = [0, 0]
#     for i in range(1, n + 1):
#         if n % i == 0 and m % i == 0:
#             answer[0] = i
#             answer[1] = i * (n // i) * (m // i)
#     return answer


# 유클리드 호제법
def gcd(n,m):
    mod = m%n
    if mod != 0:
        m,n = n,mod
        return gcd(n,m)
    else:   # mod == 0이면 작은 수가 최대공약수가 되니깐
        return n

def solution(n,m):
    return [gcd(n,m) , int(m*n/gcd(n,m))]


n,m = 3,12
# n,m = 2,5
print(solution(n,m))