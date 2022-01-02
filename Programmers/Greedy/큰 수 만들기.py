# level 2

# 조합으로 풀었는데 시간 초과

# from itertools import combinations
# def solution(number, k):
#     n = len(number)
#     answer = list(combinations(list(number), n - k))
#
#     return "".join(sorted(answer, reverse=True)[0])


# def solution(number, k):
#     answer = []
#     for i in range(len(number)):
#         while answer and k > 0 and number[i] > answer[-1]:
#             answer.pop()
#             k-=1
#         answer.append(number[i])
#     return "".join(answer[:len(answer)-k])

def solution(number,k):
    answer = []
    for num in number:
        while answer and k>0 and answer[-1]<num:
            answer.pop()
            k-=1
        answer.append(num)
    answer = "".join(answer[:len(number)-k])
    return answer

number = "1231234"
k = 3
print(solution(number, k))