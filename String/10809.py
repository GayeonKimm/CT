#1152
# a = input().split()
# print(len(a))

# 10809
alphabet = 'abcdefghijklmnopqrstuvwxyz'
A = input()
for i in alphabet:
    if i in A:
        print(A.index(i), end =' ')
    else:
        print(-1, end=' ')

# A location!!

