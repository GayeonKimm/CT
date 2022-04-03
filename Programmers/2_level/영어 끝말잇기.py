# def solution(n, words):
#     stack = []
#     a, b = 0, 0
#     for i in range(len(words)):
#         if not stack:
#             stack.append(words[i])
#         else:
#             if words[i] not in stack and stack[-1][-1] == words[i][0]:
#                 stack.append(words[i])
#             else:
#                 a = len(stack) % n + 1
#                 b = len(stack) // n + 1
#                 break
#     return [a,b]

# method2
def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]

n, words =3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))