# moves는 열을 나타냄. move로 열에 접근하여
# stack에 일단 쌓고, 같은게 있으면 터트려 버림
# 터트릴거 answer에 추가
# answer의 총 갯수를 반환

# def solution(board, moves):
#     answer = []
#     stack = []
#     for move in moves:
#         for i in range(len(board)):
#             if board[i][move-1] > 0:
#                 stack.append(board[i][move-1])
#                 board[i][move-1] = 0
#
#                 if stack[-1:] == stack[-2:-1]:
#                     answer.append(stack[-2:])
#                     stack = stack[:-2]
#                 break # 다 확인했으면 break해서 for문 넘어가야 됨!
#     # print(answer)
#     return len(answer)*2

# 다른 풀이
def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] > 0:
                if not stack:
                    stack.append(board[j][i-1])
                else:
                    if stack[-1] == board[j][i-1]:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer

print(solution([[0,0,0,0,0],
                [0,0,1,0,3],
                [0,2,5,0,1],
                [4,2,4,4,2],
                [3,5,1,3,1]],
               [1,5,3,5,1,2,1,4]))