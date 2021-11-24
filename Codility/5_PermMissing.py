def solution(A):
    A = sorted(A)
    print(A)
    for i in range(0,len(A)):
        if A[i] != i+1:
            return i+1

    return len(A)+1

    pass


print(solution([2,3,1,5]))
print(solution([2,3,1,4]))
print(solution([2,3,1,4,6]))