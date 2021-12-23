def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            left = triangle[i-1][j-1] if j!=0 else 0
            right = triangle[i-1][j] if j!=i else 0
            print("left = ", left )
            print("right = ", right)
            triangle[i][j] = triangle[i][j] + max(left, right)
            print("### triangle[",i,"][",j,"] = ", triangle[i][j])

    print("triangle[-1] = ", triangle[-1])
    print("triangle = ", triangle)

    return max(triangle[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))