def solution(m,n,board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        remove = [[0]*n for _ in range(m)]
        # 블록 찾으면 remove 배열에 1로 표시
        # 배열의 오른쪽과 하단 끝은 비교할 것이 없이 때문에 range 조절
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    remove[i][j], remove[i][j+1], remove[i+1][j], remove[i+1][j+1] = 1, 1, 1, 1

        # ramove 개수 세기
        count = 0
        for i in range(m):
            count += sum(remove[i])
        answer += count

        # 근데 지워질게 하나도 없다? 그럼 게임 while 종료
        if count == 0:
            break

        # 블럭 채우기
        for i in range(m-1, -1, -1):
            for j in range(n):
                if remove[i][j] == 1:
                    x = i-1
                    while x >= 0 and remove[x][j] == 1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        remove[x][j] = 1
            print(remove)

    return answer


m,n,board = 4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))