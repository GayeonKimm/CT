# 이것만 풀고 다른거 해야지...

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]

    # 입력 받은데까지만 호실 만들고
      #층 쌓기
    for _ in range(k):
        for y in range(1,n):
            people[y] += people [y-1]
    print(people[-1]) #맨 마지막 값이니까

# people = [i for i in range(1, 5)]
# print(people)
# print(people[-1])

# 내가 짰는데도 모르겠다 이따 다시 보기