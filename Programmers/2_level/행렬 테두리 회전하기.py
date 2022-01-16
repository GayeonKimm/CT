def solution(rows, columns, queries):
    answer = []
    graph = [[0 for _ in range(columns)] for _ in range(rows)]

    # graph에 숫자 집어넣기
    t = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = t
            t += 1

    # 회전하기
    for x1, y1, x2, y2 in queries:
        tmp = graph[x1 - 1][y1 - 1] # 임시로 가장 작은 값 설정
        mini = tmp

        for k in range(x1 - 1, x2 - 1):
            test = graph[k + 1][y1 - 1]  # test에 숫자 저장해서
            graph[k][y1 - 1] = test    # 이동하는 코드
            mini = min(mini, test)  # mini 값 새로 갱신

        for k in range(y1 - 1, y2 - 1):  # 하단 가로
            test = graph[x2 - 1][k + 1]
            graph[x2 - 1][k] = test
            mini = min(mini, test)

        for k in range(x2 - 1, x1 - 1, -1):  # 왼쪽 세로
            test = graph[k - 1][y2 - 1]
            graph[k][y2 - 1] = test
            mini = min(mini, test)

        for k in range(y2 - 1, y1 - 1, -1):
            test = graph[x1 - 1][k - 1]
            graph[x1 - 1][k] = test
            mini = min(mini, test)

        graph[x1 - 1][y1] = tmp # 처음 숫자는 삭제될수밖에 없어서 따로 저장
        answer.append(mini)  # 최종 mini값 추가

    return answer


rows, columns = 6,6
queries =[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# rows, columns = 3,3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))