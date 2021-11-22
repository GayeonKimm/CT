def solution(N):
    binary_num = bin(N)
    arr_ =[]
    for i in range(2,len(binary_num)):
        if binary_num[i] == '1':
            arr_.append(i)

    arr2_ =[]
    for i in range(0,len(arr_)):
        if i != len(arr_)-1:
            tmp = arr_[i+1]-arr_[i]
            tmp = tmp-1
            arr2_.append(tmp)
    if len(arr2_) == 0:
        return 0
    else:
        return max(arr2_)
    pass

print(solution(1041))
print(solution(15))
print(solution(32))
