def solution(A,K):
    arr_ = list(range(len(A)))

    for i in range(0, len(A)):
        arr_[(i+K)%len(A)] = A[i]
    return arr_
    pass

print(solution([3,8,9,7,6],3))
print(solution([0,0,0],1))
print(solution([1,2,3,4],4))