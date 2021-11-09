# 화이팅

# 1152 단어의 개수
# word = input().split()
# print(len(word))
# 문제를 잘 읽어봐 여러번 등장하면 모두 세라는데 set을 해야겠니

# 2908 상수
# num1, num2 = input().split()
# num1 = int(num1[::-1])
# num2 = int(num2[::-1])
# print(num1) if num1>num2 else print(num2)

# 5622 다이얼
# word = input()
# alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# time = 0
#
# for unit in alphabet:
#     for i in unit:
#         for j in word:
#             if i==j:
#                 time += alphabet.index(unit) +3
# print(time)

# 2941 크로아티아 알파벳
a = input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for al in cro:
    for i in a:
        if al==i:
            cnt+=1
