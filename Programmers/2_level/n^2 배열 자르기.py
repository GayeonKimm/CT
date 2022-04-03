'''
이동하는게 나은지
아니면 for문으로 작성하는게 나을지
'''

def solution(n, left, right):
    answer = []
    maps = [[0]*n for _ in range(n)]
    # 넣기
    for i in range(n):
        for j in range(i):
            maps[j][i] += i
    # 빼기
    for i in range(n):
        for j in range(n):
            answer.append(maps[i][j])

    return answer[left:right+1]


n,left,right = 4,7,14
print(solution(n,left, right))