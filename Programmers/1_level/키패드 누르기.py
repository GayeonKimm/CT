def solution(numbers, hand):
    answer = ''
    graph = {1:[0,0], 2:[0,1], 3:[0,2],
            4:[1,0], 5:[1,1], 6:[1,2],
            7:[2,0], 8:[2,1], 9:[2,2],
            '*':[3,0], 0:[3,1], '#':[3,2]}
    left = graph['*']
    right = graph['#']

    now = []
    for i in numbers:
        if i in [1,4,7]:
            left = graph[i]
            answer += 'L'
        elif i in [3,6,9]:
            right = graph[i]
            answer += 'R'

        else:
            left_d = 0
            right_d = 0
            now = graph[i]

            for a,b,c in zip(left, right, now):
                left_d += abs(a-c)
                right_d += abs(b-c)
            # 계산 다 하고 if문 돌려야됨 ...!!!!!!!!!!!!!!1
            if left_d < right_d:
                left = graph[i]
                answer += 'L'
            elif left_d > right_d:
                right = graph[i]
                answer += 'R'
            else:
                if hand == 'left':
                    left = graph[i]
                    answer += 'L'
                else:
                    right = graph[i]
                    answer += 'R'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))