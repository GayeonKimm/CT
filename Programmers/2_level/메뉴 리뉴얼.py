from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        temp = []

        for order in orders:
            temp += combinations(sorted(order), c)
            # temp += combi
        counter = Counter(temp)
        print("counter = ", counter)

        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)


# counter['AB'] 하면 그 counter값 출력됨 즉 숫자가 나온다는 거야
# 그 숫자가 카운터들 중에서 최대값이랑 같으면 그 값을 내가 answer에 추가하겠다는 말임요

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders, course))