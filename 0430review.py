'''
1. 소수판별
2. 최대공약수
3. 리스트 양쪽 비교
4. sort key 로 이것저것
--
5.  bfs, dfs 코드 외워두기 다시
6. pop, popleft 기강 잡기 <--- deque 사용법
---
7. 간단했던 코드들, split('0') or count('0') or index('0')
이런 것도 다시 한 번씩 볼 것
'''

# 1. 소수 판별코드
r = [i for i in range(20)]
answer = []
for i in r:
    if i < 2:
        continue # 2보다 작으면 다음 루프로 continue.
    # 2보다 작으면 밑에 코드 안돌아감

    chk = True
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            chk = False
            break
    if chk: # 소수면
        answer.append(i)
print(answer)

# 2. 최대공약수 & 최소공배수
'''
1. 두 수 중에 작은수로 나눌거라 나누는 과정 필
2. 계속 나누는 while 문 작성
** 외우자 a,b = b,mod**
# 최소공배수는 두 값을 곱한것을 최대공약수로 나눈 것
'''
a,b = 14, 35
c,d = 19, 2

def gcd(x,y):
    a,b = max(x,y), min(x,y) # 작은 수는 b
    while True:
        mod = a % b
        if mod == 0:
            return b
        else:
            a,b = b, mod
print(a,b,'최대공약수 = ',gcd(a,b), '최소공배수 = ', int(a*b/gcd(a,b)))
print(gcd(c,d))

# 3 리스트 비교할 때는 range 설정 잘 하기

# 4 sort - 리스트만 됨/ dic, tuple 모두 안됨 리스트로 묶여있어야 됨
# 다중 적용
k = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0), (3, 9), (0, 7)]
print(k)
k.sort(key=lambda x: (x[0], -x[1])) # 첫번째는 오름차순, 그 뒤는 내림차순~ # 기출임
print(k)

a = {'국어': [80,72,50], '과학': [100,0,26], '영어': [72,5,88]}
print(a)
aa = list(a.items())
aa.sort(key=lambda x:x[1]) # 저 안에 리스트 어케 정렬하냐........
print(aa)
a1 = [('국어',80,72,50), ('과학',100,0,26), ('영어',72,5,88)]
a1.sort(key=lambda x:(x[0],-x[1],-x[2])) # 근데 이런거는 이름이 동등할 때 설정하는 것 같음
print(a1)

'''
완. bfs, dfs는 따로 알아보삼
'''
