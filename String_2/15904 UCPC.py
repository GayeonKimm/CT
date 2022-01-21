import sys
input = sys.stdin.readline

# temp = []
# s = input().strip()
# for i in s.split():
#     for j in i:
#         if j.isupper():
#             temp.append(j)
#
# string = 'UCPC'
# if temp in string:
#     print("I love UCPC")
# else:
#     print("I hate UCPC")

s = input().strip()
data = ['U','C','P','C']
chk = False # 먼저 선언해도 되고, 안해도 되고

for i in range(4):
    if data[i] in s:
        chk = True
        index = s.find(data[i])
        s = s[index+1::] # 뒤에 값들만 확인할 수 있도록
        # print(index)
        # print(s)
    else:
        chk = False
        break
if chk:
    print("I love UCPC")
else:
    print("I hate UCPC")