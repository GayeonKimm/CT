'''
이거는 여러번 시도했어도 모르겠는 문제
풀었는데 이해 안됨 +1

(A,E,I,O,U)
A     - 10000
AA    - 11000
AAA   - 11100
AAAA  - 11110

AAAAA - 11111
AAAAE - 11112
AAAAI - 11113
AAAAO - 11114
AAAAU - 11115
다섯개 반복하고 자릿수가 변경됨
AAAE  - 11120 10
AAAEA - 11121 11
AAAEE - 11122 12
AAAEI O U 11123 11124 11125
AAAI  - 11130 - 16
'''


def solution(word):
    n = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    answer = len(word)
    re = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1
    for i in word:
        answer += re * n[i]
        re = (re - 1) // 5

    return answer


print(solution('AAAAE'))
print(solution('AAAE'))
print(solution('AAAEA'))
print(solution('AAAI'))
print(solution('I'))

