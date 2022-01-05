# level 2
def solution(priorities, location):
    answer = 0
    from collections import deque

    q = deque([(v, i) for i, v in enumerate(priorities)])

    while len(q):
        item = q.popleft()
        if q and max(q)[0] > item[0]:
            q.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer

# 데크 안쓰고

# def solution(priorities, location):
#     answer = 0
#
#     array1 = [c for c in range(len(priorities))] # index 위치 저장
#     array2 = priorities.copy() # 값 저장 (출력되는 값)
#
#     i = 0
#     while True:
#         if array2[i] < max(array2[i+1:]):
#             array1.append(array1.pop(i))
#             array2.append(array2.pop(i))
#         else:
#             i += 1
#
#         if array2 == sorted(array2, reverse=True):
#             break
#
#     return array1.index(location) + 1



priorities =[2, 1, 3, 2]
# location = 2

# print("\n### location : 0\n")
# print(solution(priorities, 0))
# print("\n### location : 1\n")
# print(solution(priorities, 1))
print("\n### location : 2\n")
print(solution(priorities, 2))
# print("\n### location : 3\n")
# print(solution(priorities, 3))


