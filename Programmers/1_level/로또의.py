# 로또의 최고 순위와 최저 순위

# def solution(lottos, win_nums):
#     answer = []
#
#     cnt = 7
#     for j in lottos:
#         if j in win_nums:
#             cnt -= 1
#     if cnt > 6:
#         answer.append(6)
#     else:
#         answer.append(cnt)
#
#     return answer

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)

    ans = 0

    for i in win_nums:
        if i in lottos:
            ans += 1

    return rank[cnt_0 + ans], rank[ans]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))