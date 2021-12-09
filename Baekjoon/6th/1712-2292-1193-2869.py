# 1712 손익분기점
# a,b,c = map(int, input().split())
#
# if c > b:
#     print(a//(c-b)+1)
# else:
#     print(-1)

# 2292 벌집
# 수열 구하는거 말도 안돼
# 이거 진짜 개똑똑하네
# num = int(input())
# cnt = 1
# d = 6
# count = 1
# while num > cnt:
#     count += 1
#     cnt += d
#     d += 6
# print(count)

# cnt(수열값 a1,a2,a3 등)이 입력값보다 더 커지지 않게 코드 작성

# 1193 분수찾기 water fountain 아님
# 이건 도무지 먼 말인지는 모르겟으나 했음
# x = int(input())
# line = 1
# while x > line:
#     x -= line
#     line += 1
#
# if line%2 == 0:
#     a = x
#     b = line-x+1
# else:
#     a = line-x+1
#     b = x
# print(a,'/',b, sep= '') # sep은 붙여서


# 2869 달팽이는 올라가고 싶다
# 식이 너무 어렵다
# 올라간 현재 위치가 정상이면 내려오면 안됨
# 정상에 도착하면 미끄러지면 안됨 ...
a,b,v = map(int, input().split())
if (v-b)%(a-b) == 0:
    n = (v-b)//(a-b)
else:
    n = (v-b)//(a-b) + 1
print(n)
