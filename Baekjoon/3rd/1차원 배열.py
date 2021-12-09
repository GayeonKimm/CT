# 10818 최소 최대
# n = int(input())
# list = list(map(int, input().split()))
# print(max(list), min(list))

# 근데 이럴거면 n은 굳이 왜 받음? 킹받네


# 2562 최댓값
# 인덱스값 출력하는거 뭐였더라...list.index였나?
# list = []
# for i in range(9):
#     num = int(input())
#     list.append(num)
# print(max(list))
# print(list.index(max(list))+1)

# 2577 숫자의 개수
# a = int(input())
# b = int(input())
# c = int(input())
# list= list(str(a*b*c))
# # print(list)
# # print(list.count('0'))
# # 하면 0 의 갯수 카운트 옵션 사용
#
# for i in range(10):
#     print(list.count(str(i)))
# str 안하면 리스트 문자 인식 못해서 안된다 꼭 해주기


# 3052 나머지
# list1 =[]
# for i in range(10):
#     n = int(input())
#     list1.append(n%42)
# list2 = set(list1)
# print(len(list2))

# 1546 평균
# n = int(input())
# score = list(map(int, input().split()))
# m = max(score)
#
# sum = 0
# for i in range(n):
#     score[i] = (score[i]/m)*100
#     sum += score[i]
# print(sum/n)


# 8958 OX퀴즈
# n = int(input())
# for i in range(n):
#     test = list(input())
#     o_cnt = 1
#     score = 0
#     for i in test:
#         if i =='O':
#             score += o_cnt
#             o_cnt += 1
#         else :
#             o_cnt = 1
#     print(score)


# 4344 평균은 넘겠지
n = int(input())
for _ in range(n):
    score = list(map(int, input().split()))
    avg = sum(score[1:])/score[0]
    cnt = 0
    # print(avg)

    for s in score[1:]:
        if s > avg:
            cnt += 1
    rate = (cnt/score[0])*100
    print(f'{rate:.3f}%')

# 이거 잘했다 담에 또 풀어보기