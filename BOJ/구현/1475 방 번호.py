import sys
input = sys.stdin.readline
# s = map(int, input().strip())
# answer = 1
# temp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in s:
#     check = False
#     if i in temp:
#         temp.remove(i)
#     else:
#         if i == 6:
#             if 9 in temp:
#                 temp.remove(9)
#             else:
#                 check = True
#         elif i == 9:
#             if 6 in temp:
#                 temp.remove(6)
#             else:
#                 check = True
#         else:
#             check = True
#     if check:
#         answer += 1
#         temp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         temp.remove(i)
#     # print(i, temp, answer)
# print(answer)


s = input().strip()
dic = {'0' : 0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}
for i in range(len(s)):
    if s[i] in ['6', '9']:
        dic['6'] += 1
    else:
        dic[s[i]] += 1
# print(dic)
if dic['6'] % 2 == 0:
    dic['6'] = dic['6'] // 2
else:
    dic['6'] = dic['6'] // 2 + 1

print(max(dic.values()))