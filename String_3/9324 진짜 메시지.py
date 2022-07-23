'''
문자열 확인/ 등장 횟수 먼저 카운팅
- 세번째 count인데 마지막 문자열이야
- 세번째 count인데 다음게 다르면

d 쓰면 틀리고
count 함수 -> 시간 초과
count(m[i], 0, i)+1 -> 시간초과 ...
'''

import sys
input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     m = input().strip()
#     chk = True
#
#     for i in range(len(m)):
#
#         # 마지막 글자인데 등장횟수가 3번째면 break지
#         if (m.count(m[i], 0, i)+1) % 3 == 0:
#             if i == len(m)-1:
#                 chk = False
#                 break
#             if m[i] != m[i+1]:
#                 chk = False
#                 break
#
#     if chk:
#         print('OK')
#     else:
#         print('FAKE')


for _ in range(int(input())):
    m = input().strip()
    chk = False
    msg = [0 for _ in range(26)]
    res = 'OK'
    for i in range(len(m)):
        if chk:
            chk = False
            continue
        msg[ord(m[i])-65] += 1

        if msg[ord(m[i])-65] == 3:
            if i == len(m)-1:
                res = 'FAKE'
                break
            elif m[i] != m[i+1]:
                res = 'FAKE'
                break
            chk = True
            msg[ord(m[i])-65] = 0

    print(res)