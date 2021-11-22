def solution(N):
    binary_num = bin(N)
    for i in range(2,len(binary_num)):
        if binary_num[i]=='1':
            arr_.append(i)


    pass
solution(32)
