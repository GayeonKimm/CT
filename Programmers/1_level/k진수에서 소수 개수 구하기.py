'''
+ 5
1. 진수 변경
2. 소수인 것 아닌것 나눠서 check에 저장
- 소수 판별 코드
---> 0을 기준으로 숫자를 나눈다 (개 간단한 것을 ..... 시바)
4. 소수 판별
해당 코드가 0또는 1이거나 빈공간이면 continue
'''

def solution(n, k):
    answer = 0
    # 변경
    temp = ''
    while n:
        temp = str(n%k) + temp
        n = n // k

    # 0을 기준으로 분리 - 얼탱이가 없는 코드
    # ck = ''
    # check = []
    # for i in temp:
    #     if i != '0':
    #         ck += i
    #     else:
    #         check.append(int(ck))
    #         ck = ''
    #         check.append(int(i))
    word = temp.split('0')

    for i in word:
        if len(i) == 0 or int(i) < 2:
            continue  # pass 쓰면 안됨요

        chk = True
        # i = int(i) # 해도 됨
        for j in range(2, int(int(i)**0.5)+1):
            if int(i) % j == 0:
                chk = False
                break
        if chk:
            answer += 1

    return answer

n,k = 437674,3
print(solution(n, k))