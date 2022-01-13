def gcd(w,h):
    a,b = max([w,h]), min([w,h])
    while True:
        mod = a%b
        if mod == 0:
            return b
        else:
            a,b = b, mod

def solution(w,h):
    squares = w*h
    tmp = gcd(w,h)
    return squares - (w+h-tmp)



print(solution(8,12))
