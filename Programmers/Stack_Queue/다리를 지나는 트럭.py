# level 2

# 데크 사용
# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     trucks = deque(truck_weights)
#     wait = deque()
#     sum_weight =0
#     time = 0
#
#     while trucks:
#         time += 1
#
#         while wait and wait[0][0] <= time:
#             t,w = wait.popleft()
#             sum_weight -= w
#
#         if sum_weight + trucks[0] <= weight:
#             truck = trucks.popleft()
#             wait.append((bridge_length + time, truck))
#             sum_weight += truck
#     return wait[-1][0]

# 스택 사용
def solution(bridge_length, weight, truck_weights):
    answer = 0
    tonb = [0]*bridge_length

    while len(tonb):
        answer += 1
        tonb.pop(0)
        if truck_weights:
            if sum(tonb) + truck_weights[0] <= weight:
                tonb.append(truck_weights.pop(0))
            else:
                tonb.append(0)

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))