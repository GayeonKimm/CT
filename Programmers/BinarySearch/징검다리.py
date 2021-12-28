# level 4

def check(term, rocks):
    count = 0
    start = 0
    minval = 1e9
    for i in range(len(rocks)):
        if rocks[i] - start < term:  # start위치부터 못건널때까지 체크(지나가는 돌들 체크)
            count += 1
        else:
            minval = min(minval, rocks[i] - start)
            start = rocks[i]
    return count, minval


def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()

    left = 0
    right = distance
    while left <= right:
        mid = (left + right) // 2
        count, minval = check(mid, rocks)
        if count > n:
            right = mid - 1
        else:
            answer = minval
            left = mid + 1
    return answer


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))