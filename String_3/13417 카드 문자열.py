'''
들어갈때 맨 앞의 결과보다 더 빠르면 맨 앞에 넣고
더 느리면 맨 뒤에 넣고 -> ord로 계산

한번에 맞춰버렸 아이캔두잇
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    cards = input().strip().split()

    answer = []
    for i in range(n):
        if i == 0:
            answer.append(cards[0])
        else:
            if ord(cards[i]) > ord(answer[0]): # 크면
                answer.append(cards[i])
            else:
                answer.insert(0, cards[i])

    print(''.join(answer))