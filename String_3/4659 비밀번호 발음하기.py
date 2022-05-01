'''
1. aeiou 포함
2. 3연속 모음 or 자음 오면 안됨
3. 같은 글자 ㄴㄴ -ee, oo 허용
chk1 , chk2

모음 있으면
1. 모음이 연속으로 3개 안됨 **
2. 같은 글자가 연속이면 안됨 - e, o 허용


1. 자음이 연속으로 3개 안됨 **
2. 같은 글자가 연속이면 안됨
'''
import sys
input = sys.stdin.readline

vowels = 'aeiou'
while True:
    word = input().strip()
    chk1, chk2 = False, True

    if word == 'end':
        break

    for i in word:
        if i in vowels:
            chk1 = True
    if chk1:
        for i in range(len(word)-1):
            if word[i] == word[i+1] and word[i] not in 'eo': # e, o 안들어가면 False 지
                chk2 = False

    for i in range(len(word)-2):
        if word[i] in vowels and word[i+1] in vowels and word[i+2] in vowels:
            chk2 = False
        elif word[i] not in vowels and word[i+1] not in vowels and word[i+2] not in vowels:
            chk2 = False

    if chk1 == True and chk2 == True:
        print('<%s> is acceptable.' %word)
    else:
        print('<%s> is not acceptable.' %word)