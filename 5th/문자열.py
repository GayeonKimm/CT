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
# alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# word = input()
# time = 0
#
# for unit in alphabet:
#     for i in unit:
#         for j in word:
#             if i==j:
#                 time += alphabet.index(unit) +3
# print(time)

# 2941 크로아티아 알파벳
# 처음엔 a, k 이런것도 알파벳 추가해야하는줄 .. 나 문해력 무슨일이냐
# 그냥 len 하면 되는거 같음

# cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# word = input()
# for i in cro:
#     word = word.replace(i,'*')
# print(len(word))

# replace 쓰는거 신기하당 cnt해서 검정하려고 했는데


# 1316 그룹 단어 체커
# 진짜 모르겠다 시간좀 걸림

n = int(input())
result = 0
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result += 1
            break
print(n-result)

# 해냅니다 김가연이죠!!!!!!!!!!!!11