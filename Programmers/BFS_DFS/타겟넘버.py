# 타겟 넘버


# def solution(numbers, target):
#     S = sum(numbers)
#     L = [S]  # [5]
#     print(len(L))
#
#     for n in numbers:
#         Len = len(L)
#         for idx in range(Len):
#             L.append(L[idx]-2*n)   # 왜 2*n 일까
#         print(L)
#     return L.count(target)

# method 1 DFS
def dfs(idx, ans):
    global answer, nb, tg
    if idx == len(nb):
        if ans == tg:
            answer += 1
        return
    else:
        dfs(idx+1, ans+nb[idx])
        dfs(idx+1, ans-nb[idx])
        return

def solution(numbers, target):
    global answer, nb, tg
    nb = numbers
    tg = target
    answer = 0
    dfs(0,0)
    return answer

# method 2
# def solution(numbers, target):
#     if not numbers and target == 0:
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))