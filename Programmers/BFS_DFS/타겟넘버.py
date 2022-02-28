# 타겟 넘버
# DFS
def dfs(idx, ans):
    global answer
    if idx == len(numbers):
        if ans == target:
            answer += 1
        return
    else:
        dfs(idx + 1, ans + numbers[idx])
        dfs(idx + 1, ans - numbers[idx])
        return

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, 0)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))