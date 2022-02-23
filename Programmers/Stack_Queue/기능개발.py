# def solution(progresses, speeds):
#     stack = []
#     d = dict()
#     for i in range(len(progresses)):
#         time = (100 - progresses[i]) // speeds[i]
#         if (100 - progresses[i]) % speeds[i] > 0:
#             time += 1
#
#         if len(stack) == 0 or time > stack[-1]:
#             stack.append(time)
#             d[time] = 1
#         else:
#             d[stack[-1]] += 1
#
#     return [v for k, v in d.items()]

# 다시 푼 풀이 +3
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses) > 0:
        if (progresses[0] + speeds[0]*time) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1

    answer.append(count)
    return answer


progresses =[93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))
