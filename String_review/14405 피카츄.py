'''
피카추 문자열로만 구성된 s찾기
문자열이 존재하면 *로 대체해 둔 다음 *말고 다른게 존재하면 NO 출력하기
'''
import sys
input = sys.stdin.readline

pocket = ['pi', 'ka', 'chu']
s = input().strip()
for i in pocket:
    if i in s:
        s = s.replace(i, '*') # 별로 대체 하는 방법쓰

chk = True
for i in s:
    if i != '*': # 아닌게있다면
        chk = False
        break

if chk:
    print("YES")
else:
    print("NO")