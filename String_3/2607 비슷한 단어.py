'''
Counter를 통해 문자의 갯수를 세어둠
그리고 keys로 접근해서 그 값을 더하고 뺐을때 조건을 만족하면 answer 증가
더하는건 ㅇㅋ인데 빼서 0이 되어버리면 어카냐
'''
# import sys
# input = sys.stdin.readline
# from collections import Counter
#
# n = int(input())
# c = input().strip()
# check = Counter(c)
# answer = 0
# for _ in range(n-1):
#     t = input().strip()
#     temp = Counter(t)
#     if check == temp:
#         answer += 1
#     elif set(c) == set(t):
#         for i in check.keys():
#             if check[i] + 1 == temp[i] or check[i]-1 == temp[i]:
#                 answer += 1
#                 break
# print(answer)

import sys
input = sys.stdin.readline

n = int(input())
word = input().strip()
answer = 0
for _ in range(n-1):
    word2 = input().strip()
    word_list = list(word)
    count = 0
    for i in word2:
        if i in word_list:
            word_list.remove(i)
        else:
            count += 1

    if count <= 1 and len(word_list) <= 1:
        answer += 1
print(answer)


