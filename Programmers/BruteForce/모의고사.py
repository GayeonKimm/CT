def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    ret = [0,0,0]

    for i in range(len(answers)):
        # 여기 elif 의 방식대로 짜면 3명중 한명만 맞게됨
        # 모두 통과하게 해줘야 모두 정답 인정 된다
        if answers[i] == first[i%len(first)]:   # first의 반복수만큼 나눠줘야함
            ret[0] += 1
        if answers[i] == second[i%len(second)]:
            ret[1] += 1
        if answers[i] == third[i%len(third)]:
            ret[2] += 1

    max_value = max(ret)
    answer = []
    for i in range(len(ret)):
        if ret[i] == max_value:
            answer.append(i+1)

    return answer

# answers = [1,2,3,4,5]
answers = [1, 3, 2, 4, 2]
print(solution(answers))


# 1. i%5 <-- idea! (각 상황이 몇개씩 반복되느냐에 따라 다르게 설정할 것!)
# 2. ret[]
# 3. make a max_value --> max_value = max(ret)
# 4. compare max_value with ret[i]


# first idea

# for people in first:
#     cnt = 0
#     for i in range(len(people)):
#         if answers[i] == people[i]:
#             cnt += 1
#     co.append(cnt)


# other method
# def solution(answers):
#     m1 = [1,2,3,4,5]
#     m2 = [2,1,2,3,2,4,2,5]
#     m3 = [3,3,1,1,2,2,4,4,5,5]
#     r1=r2=r3=0
#     for i,a in enumerate(answers):
#         if m1[i%5] == a:
#             r1 += 1
#         if m2[i%8] == a:
#             r2 += 1
#         if m3[i%10] == a:
#             r3 += 1
#     M = max(r1,r2,r3)
#     answer = []
#     if M == r1:
#         answer.append(1)
#     if M == r2:
#         answer.append(2)
#     if M == r3:
#         answer.append(3)
#     return answer