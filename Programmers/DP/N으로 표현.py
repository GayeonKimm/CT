# level 3
# *****

def solution(N, number):
    if N == number:
        return 1

    s = [set() for i in range(8)]
    print("s = ", s)

    for x in range(len(s)):
        s[x].add(int(str(N)*(x+1)))
    print("s = ", s)

    for i in range(1,len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-1-j]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        print(s)
        # 계속 i = 1 , 2 , 3
        # number인게 있으면 i+1 만해서 결과 출력
        if number in s[i]:
            return i+1
    return -1

N = 5
number = 12
print(solution(N, number))