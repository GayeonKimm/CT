'''
1. while 로 s가 1이 될 때까지 루프
2. 0을 제거
3. 이진 표현

자꾸 for문으로 확인하려하지말고
count좀 써먹자~~~~!!
응? 응 ???????????!!!!!
'''

def solution(s):
    answer, cnt = 0, 0
    while s != '1':
        # temp = ''
        # for i in s:
        #     if i == '0':
        #         cnt += 1
        #     else:
        #         temp += i
        # c = len(temp)

        c = s.count('1')
        cnt += len(s) - c
        s = bin(c)[2:]
        answer += 1
    return [answer, cnt]

print(solution('0111010'))
