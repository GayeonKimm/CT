# method
def solution(x):
    answer = [int(i) for i in str(x)]
    if x % sum(answer) == 0:
        return True
    else:
        return False

print(solution(12))