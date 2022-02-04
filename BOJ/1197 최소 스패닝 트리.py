import sys
input = sys.stdin.readline

V, E = map(int, input().split())
Vroot =  [i for i in range(V+1)]
Elist = [list(map(int, input().split())) for _ in range(E)]
# 가중치를 기준으로 정렬
Elist.sort(key=lambda x:x[2])

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w

print(answer)