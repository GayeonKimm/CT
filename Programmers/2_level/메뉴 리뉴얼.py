# 재풀이 +3
"""
1. order들을 course에 맞게 combinations
2. counter를 사용해 갯수 셈
3. 조건
- 최소 2명이상에게서 발생할 것
- 최다 주문 메뉴만 추가할 것
- 마지막엔 sort 오름차순
"""

from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for j in orders:
            temp += list(combinations(sorted(j), i))
        c = Counter(temp)

        if len(c) != 1 and max(c.values()) != 1:
            answer += [''.join(i) for i in c if c[i] == max(c.values())]

    return sorted(answer)

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders, course))