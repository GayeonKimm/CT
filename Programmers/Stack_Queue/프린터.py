# level 2

# 데크 사용해서 하나 먼저 pop해서 max값 비교한뒤
# max가 더 크면 그 하나 맨뒤로 append
# 이때 location 위치를 찾기 위해 index랑 같이 for문 돌림
# location이 우리가 원하는거면 break로 종료해도 됨

def solution(priorities, location):
    from collections import deque
    q = deque([(v,i) for i,v in enumerate(priorities)])
    answer = 0

    while q:
        temp = q.popleft()
        if temp[0] < max(q)[0]:
            q.append(temp)
        else:
            answer += 1
            if temp[1]==location:
                break
    return answer


# priorities, location = [2, 1, 3, 2], 2
priorities, location = [1, 1, 9, 1, 1, 1],0
print(solution(priorities, location))


