# level 2

# 조합으로 풀었는데 시간 초과

# from itertools import combinations
# def solution(number, k):
#     n = len(number)
#     answer = list(combinations(list(number), n - k))
#
#     return "".join(sorted(answer, reverse=True)[0])

def solution(number,k):
    answer = []
    for num in number:
        while answer and k>0 and answer[-1]<num:
            answer.pop()
            k -= 1
        answer.append(num)

    # 이거 안쓰면 마지막에 오류 하나 남
    # 길이만큼만 걍 잘라서 출력해야해서
    print("".join(answer))
    # 이렇게 해도 되는데 범위 지정 안하면 하나 틀리긴 하네
    
    return "".join(answer[:len(answer)-k])


number = "1231234"
k = 3
print(solution(number, k))