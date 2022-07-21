'''
기본 변수형 + 기본 변수명 + 변수선언
공통된 변수형 +타입
이때 타입은 [], &, *
'''

import sys
input = sys.stdin.readline

string = input().strip()
string_list = string.split(' ')

# 기본 변수형만 따로 basic_type 으로 저장
basic_type = string_list[0]
del string_list[0]

for s in string_list:
    s = s.replace(",", '').replace(";", '')

    # 기본 변수형 추가 answer 빈거 만들고 추가해도 됨
    answer = basic_type

    for i in range(len(s)-1, 0, -1):
        if not s[i].isalpha():
            if s[i] == ']':
                answer += '['
            elif s[i] == '[':
                answer += ']'
            else:
                answer += s[i]

    # 공백 추가
    answer += ' '

    # 기본 변수명(알파벳)
    for i in range(len(s)):
        if s[i].isalpha():
            answer += s[i]

    # 문단 마지막 세미콜론
    answer += ';'
    print(answer)