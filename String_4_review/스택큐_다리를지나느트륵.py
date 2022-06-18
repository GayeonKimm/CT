def solution(bridge_length, weight, truck_weights):
    answer = 0
    tonb = [0 for _ in range(bridge_length)]

    while tonb:
        answer += 1
        tonb.pop(0)
        if truck_weights:
            if sum(tonb) + truck_weights[0] <= weight:  # 올라타도 되는거
                tonb.append(truck_weights.pop(0))
            else:  # 못 올라가면
                tonb.append(0)

    return answer