from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([(p, i) for i, p in enumerate(priorities)])

    while q:
        temp = q.popleft()
        if q and (max(q)[0] > temp[0]):  # q가 비어있는 상황이 있을까봐. q가 있고, 뒤에 조건 만족하면
            q.append(temp)
        else:
            answer += 1
            if temp[1] == location:
                break
    return answer

