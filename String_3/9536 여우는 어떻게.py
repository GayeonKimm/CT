'''
들어오는 애들을 차례로 삭제시켜
replace가 있고 - > 안됨

나처럼 들어온거 확인해도 되는 방법있고,
sound를 돌면서 temp에 포함되지 않는 것들만 프린트하기
이때 temp에는 울음소리 저장 (set으로 설정해서 중복 안ㄷ되게)

여기사 remove, replace, add, 등등 정리하기~~
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    sound = input().strip().split()
    # what does the fox say? 문장이 나올 때까지 삭제시킴
    while True:
        temp = input().split()
        # print(temp)
        if temp[0] != 'what':
            break
        else:
            if temp[-1] in sound:
                while temp[-1] in sound:
                    sound.remove(temp[-1])
    for i in sound:
        print(i, end = ' ')
