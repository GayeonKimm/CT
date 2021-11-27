def solution(A):
    row =[]
    for p in range(5):
        r1 = 0
        for q in range(3):
            r1 += A[p][q]
        row.append(r1)
    # print(row[:1])
    # print(row[2:])
    # print(sum(row[2:]))

    col = []
    for q in range(3):
        c1 = 0
        for p in range(5):
            c1 += A[p][q]
        col.append(c1)
    # print(col)
    # print(col[:1])
    # print(sum(col[2:]))
    # print(sum(row[2:]))

    ans = 0
    for i in range(len(row)):
        for j in range(len(row)):
            if sum(row[:i]) == sum(row[i+1:]) and sum(col[:i]) == sum(col[i + 1:]):
                print(i,j)

    pass

print(solution([[2, 7, 5], [3, 1, 1], [2, 1, -7], [0, 2, 1], [1, 6, 8]]))