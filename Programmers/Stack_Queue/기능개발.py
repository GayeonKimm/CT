def solution(progresses, speeds):
    stack = []
    d = dict()
    for i in range(len(progresses)):
        time = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] > 0:
            time += 1

        if len(stack) == 0 or time > stack[-1]:
            stack.append(time)
            d[time] = 1
        else:
            d[stack[-1]] += 1

    # return d
    # return [v for k, v in sorted(d.items())]
    return [v for k, v in d.items()]

# no sorted okay..... why

progresses =[93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))


# 1. stack empty list
# 2. make formula (with exception)
# 3. using stack[-1] idea!
# 4. transform dict{} into list[]
