# # 5430
T = int(input())
for _ in range(T):
    Func = input()
    N = int(input())
    arr = input().rstrip()[1:-1].split(",")

    if N == 0:
        arr =[]

    l, r, re = 0, 0, True

    for i in Func:
        if i == 'R':
            re = not re
        else:
            if re is True:
                l += 1
            else:
                r += 1
    if r + l <= N:
        answer = arr[l:N - r]
        if re is True:
            print("["+",".join(answer) + "]")
        else:
            print("[" + ",".join(answer[::-1]) + "]")
    else:
        print('error')


# a =[1,2,3,4,5,6,7]
# print(a[::-1])
# print(a[:0:-1])