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
    answer = 1
    squares = w * h
    tmp = gcd(w, h)

    # return w * h - (w // tmp + h // tmp - 1) * tmp
    return w*h - (w+h-tmp)
    # 이거 걍 이거 아니냐고~

print(solution(8,12))
