# 간단한데 꼭 알아야 하는 코드



def solution(arr1, arr2):
    answer = arr1
    # answer = [[]]
    # 이게 디폴트였는데 이대로 하면 list range 오류남!

    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

# answer 설정안하고 arr1에 arr2를 더하는 방식으로도 풀더라
arr1, arr2 = [[1,2],[2,3]],[[3,4],[5,6]]
print(solution(arr1, arr2))
