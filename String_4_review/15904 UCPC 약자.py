'''
인덱스 이동해서 새로운 문자열로 저장하는 문제
찾고 싶은 문자 4개를 data 리스트에 저장해두고
돌아가면서 해당 문자열이 있는지 확인
- 새로운 문자열로 재정의 하는 이유 : 앞에 나온 문자가 중복되면 안되니까 -> 순서도 중요해서
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