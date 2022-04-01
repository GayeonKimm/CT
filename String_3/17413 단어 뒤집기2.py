import sys
input = sys.stdin.readline
'''
tag 의 유무로 판단하자

F일때 (공백 신경써야됨)
1. <가 들어오면 
- True로 변경
- b에 그대로 저장
2. 그냥 문자들어오면 
- b에 거꾸로 저장
3. 공백 들어오면
- answer에 저장하고 b 초기화

T일때 (공백 신경 안써도 됨)
1. 그냥 문자 들어오면
- b 그대로 저장
2. >가 들어오면
- False로 변경
- answer에 저장하고 b 초기화

마지막엔 b에 저장되어 있는 값까지 함께 프린트
'''
s = str(input().strip())
answer = ''
b = ''
tag = False

for i in s:
    if tag == False:
        if i == '<':
            tag = True
            b = b + i

        elif i == ' ':
            b = b + i # 공백은 그대로 뒤에 붙이기만
            answer = answer + b
            b = ''
        else:
            b = i + b

    else:
        # 괄호값이 True면 일단 그대로 넣고 봄
        b = b + i
        if i == '>':
            tag = False
            # 이미ㅣ 넣었으니까 바로 answer에 넣어도 됨
            answer = answer + b
            b = ''
if b:
    answer += b

print(answer)
