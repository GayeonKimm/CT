'''
인덱스 이동해서 저장하는 거!!!!!!!!!!!!!!!!!!!!!!!!
'''
import sys
input = sys.stdin.readline

s = input().strip()
# answer = ''
# for i in s:
#     if i.isupper():
#         if i in 'UPCP':
#             answer += i
# if answer == 'UCPC':
#     print('I love UCPC')
# else:
#     print('I hate UCPC')

chk = False
data = ['U', 'C', 'P', 'C']
for i in range(4):
    if data[i] in s:
        chk = True
        index = s.find(data[i])
        s = s[index+1:]
    else:
        chk = False
        break
if chk:
    print('I love UCPC')
else:
    print('I hate UCPC')