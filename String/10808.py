# 10808 알파벳 개수
# alphabet ='abcdefghijklmnopqrstuvwxyz'
# A = input()
# cnt = []
# for i in range(len(alphabet)):
#     cnt.append(0)
#
# for i in len(alphabet):
#     if i in A:
#         k = alphabet.index(i)
#         print(k)
#         cnt[k]
#         print(cnt)
#     else:
#         pass
# print(cnt)
# ERROR CODE


alphabet ='abcdefghijklmnopqrstuvwxyz'
A = input()
for i in range(len(alphabet)):
    cnt = A.count(alphabet[i])
    print(cnt, end =' ')

# other. 아스키 코드
str = input()
result = [0] * 26
print(result)
#
# for i in range(str):
#     result[ord(i) - 97] = str.count(i)
#
# for i in result:
#     print(i, end=" ")