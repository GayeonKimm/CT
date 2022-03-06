def solution(n):
    maps = [[0]*n for _ in range(n)]
    num = 1
    x, y = -1, 0

    for i in range(n):
        for _ in range(i, n):
            # 내려가기
            if i % 3 == 0:
                x += 1
            # 오른쪽으로
            elif i % 3 == 1:
                y += 1

            # 대각선 위로
            elif i % 3 == 2:
                x -= 1
                y -= 1

            maps[x][y] = num
            num += 1
    answer = []
    for i in maps:
        answer += [j for j in i if j != 0]
    return answer

print(solution(5))