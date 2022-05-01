'''
자바)
첫단어 소문자, 다음단어부터는 첫문자만 대문자
모든 단어는 붙여서
javaIdentifier
씨쁠쁠)
소문자만 사용, _ 사용

자바일때
문장에 대문자 있는데 _없을 때
씨쁠일때
문장에 대문자 없고 _있을 때

그 대문자 전에 _ 붙이고 소문자로 변경
- 2. 문자에 _있고 모두 소문자면 씨쁠쁠
_있는거 없애고 그 다음문자 대문자로 변경

case of "error!"
- 첫 글자문장에 소문자 아닐때
- 첫글자나 맨 마지막에 _ 있을 때
- 중간에 _가 연속해서 2개 이상 있을 떄
- _가 있는데 대문자가 존재할 때

'''

import sys
input = sys.stdin.readline

st = input().strip()
# C++일때, 자바로
# _있으면 없애고 + 대문자로
def tojava(s):
    # _가 있는데 첫글자, 마지막 글자, 연속해서
    if s[0] == '_' or s[-1] == '_' or '__' in s:
        return "Error!"

    answer = ''
    chk = False

    for i in s:
        if i.isupper(): # 여기도 꼭!!!!!!
            return "Error!"

        if i == '_':
            chk = True
            continue

        if chk == True:
            answer += i.upper()
            chk = False
            continue

        answer += i
    return answer

# 자바일때, 씨쁠로
# 대문자는 _ + 소문자로
def tocplpl(s):
    # 첫글자가 대문자면 에러임
    if s[0].isupper():
        return "Error!"

    answer = ''
    for i in s:
        if i.isupper():
            answer += '_' + i.lower()
        else:
            answer += i
    return answer

# 판단때리는 함수
if '_' in st:
    print(tojava(st))
else:
    print(tocplpl(st))
