def solution(A):
    dic = {}

    for i in A:
        try:
            dic[i] += 1
        except:
            dic[i] = 1

    for i in dic:
        if dic[i] % 2 == 1:
            return i

    pass

print(solution([9,3,9,3,9,7,9]))
