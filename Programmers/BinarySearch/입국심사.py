# 입국심사
# method 1
def check(t, times):
    ret = 0
    for time in times:
        ret += t // time
    return ret


def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n  # 가장 오래걸리는 사람이 모두 처리하는 상황

    while left <= right:
        mid = (left + right) // 2
        chk = check(mid, times)

        if chk < n:
            left = mid + 1
        else:  # n명보다 많이 처리할 수 있다면(answer는 될 수 있지만, 더 작은 것 찾기)
            answer = mid
            right = mid - 1
    return answer


# method 2
# def solution(n, times):
#     answer = 0
#     left, right = 1, max(times)*n
#
#     while left <= right:
#         mid = (left +right)//2
#         people = 0
#         # print("mid = ", mid)
#         for time in times:
#             people += mid//time
#             if people >= n:
#                 break
#         # print("people = ", people)
#
#         if people >= n:
#             answer = mid
#             right = mid -1
#         elif people < n :
#             left = mid +1
#
#     return answer



n=6
times = [7,10]
print(solution(n, times))