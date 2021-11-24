def solution(A):

    # if two elements
    if len(A) == 2:
        return abs(A[0]-A[1])

    arr = []
    tmp_1 = 0
    tmp_2 = sum(A)
    for i in range(len(A)-1):
        tmp_1 += A[i]
        tmp_2 -= A[i]
        arr.append(abs(tmp_1-tmp_2))

    return min(arr)
    pass

print(solution([3,1,2,4,3]))
print(solution([3,4]))