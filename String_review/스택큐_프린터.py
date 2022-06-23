'''
인덱스 값고 같이 비교하고 싶어서 enumerate 사용
max로 최대 큐값 찾아서 우선 순위 큐로 설정
이를 다음것과 비교하면서 있으면, 내보내고, 없으면 다시 큐에 append
- 이때 이미 뽑아놓은 q에 더는 비교할 대상이 없는 상황에 대비해
- q가 존재한다는 조건을 추가해야 함
'''

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

