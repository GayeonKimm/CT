# math 메소드 사용하기

from math import sqrt
def solution(n):
    if sqrt(n)%1 == 0:
        return int(sqrt(n)+1)**2
    else:
        return -1

# math안쓰고 하면 +1점 주더라고

print(solution(121))
# print(solution(3))