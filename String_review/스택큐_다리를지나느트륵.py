'''
다리를 건넌다는 것은 = 다리가 대기 상태에 있다는 것 그 만큼 리스트를 만들어줘야함
- truck이 존재할 때 까지
'''

def solution(bridge_length, weight, truck_weights):
    answer = 0
    tonb = [0 for _ in range(bridge_length)]

    while tonb:
        answer += 1
        tonb.pop(0) # 이거 없으면 while 문 계속 돈다
        if truck_weights:
            if sum(tonb) + truck_weights[0] <= weight:  # 올라타도 되는거
                tonb.append(truck_weights.pop(0))
            else:  # 못 올라가면
                tonb.append(0)

    return answer