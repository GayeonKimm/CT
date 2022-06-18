'''
1. 전체의 정보를 담을 d1 만들고, 뭐가 제일 많이 들어있는지에 대한 d2를 만들어둠
2. d2 많은 순으로 정렬
3. d2 돌면서 d1 정렬
4. answer에 인덱스를 넣되 각 genre에서 2개씩만
'''
def solution(genres, plays):
    answer = []
    d1, d2 = {}, {}

    for idx, (g,p) in enumerate(zip(genres, plays)):
        # d1 담기
        if g not in d1:
            d1[g] = [[idx, p]]
        else:
            d1[g].append([idx, p])

        # d2 담기
        if g not in d2:
            d2[g] = p
        else:
            d2[g] += p

    d2 = sorted(d2.items(), key=lambda x: -x[1])
    for k, p in d2:
        for idx, p in sorted(d1[k], key=lambda x: -x[1])[:2]: # 장르변 2개씩만 담아야해서
            answer.append(idx)
    return answer


genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays))