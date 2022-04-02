'''
LRU 가장 오랫 동안 참조되지 않은 페이지를 교체
딱 봐도 큐 사용하는 문제임요
'''
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    if cacheSize == 0:
        return len(cities)*5
    else:
        for i in cities:
            i = i.lower()
            if i in q:
                answer += 1
                q.remove(i)
            else:
                answer += 5
                if len(q) >= cacheSize:
                    q.popleft()
            q.append(i)
    return answer


cacheSize, cities = 3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))