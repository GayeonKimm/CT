def solution(X,Y,D):

    a = (Y-X)/D
    if a % 1 == 0:
        return int(a)
    else:
        return int(a) + 1
    pass

print(solution(10,85,30))
print(solution(10,40,10))
print(solution(10,40,10))
