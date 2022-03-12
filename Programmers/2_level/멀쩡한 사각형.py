# 재풀이 +9
def gcd(w, h):
    a, b = max(w, h), min(w, h)
    while True:
        mod = a % b
        if mod == 0:
            return b
        else:
            a, b = b, mod

def solution(w, h):
    tmp = gcd(w, h)
    return w*h - (w+h-tmp)
print(solution(8,12))
