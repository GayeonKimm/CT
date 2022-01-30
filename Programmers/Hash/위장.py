# 위장
# level 2

def solution(clothes):
    d = {}
    for name, item in clothes:
        d[item] = d.get(item, 0) + 1
        # d.get(): item의 value넣기
        # d[item], 즉 item value에 item

    answer = 1
    for item, n in d.items():
        answer *= (n+1)

    return answer - 1

clothes = [["yellowhat", "headgear"],
           ["bluesunglasses", "eyewear"],
           ["green_turban", "headgear"]]
print(solution(clothes))

