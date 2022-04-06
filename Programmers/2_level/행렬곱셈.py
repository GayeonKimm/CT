def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(arr1[i])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

# numpy 사용해서 행렬 곱하는 법
import numpy as np
# array로 변환
arr1 = np.array([[2, 3, 2], [4, 2, 4], [3, 1, 4]])
arr2 = np.array([[5, 4, 3], [2, 4, 1], [3, 1, 1]])

# 두 행렬의 곱
m = np.matmul(arr1, arr2)
print(m)

# 배열 내적, 2d는 행렬 곱과 같은 결과
d = np.dot(arr1, arr2)
print(d)

arr1, arr2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))