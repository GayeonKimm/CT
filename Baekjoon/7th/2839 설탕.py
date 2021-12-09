
# 5의 배수인지 확인하고 맞으면 계속추가
# 5의 배수 아니면 3을 빼서 5의 배수가 맞을때 까지 맞춤
# 그랬는데도 5의 배수가 안된다? 그러면 -1 출력

n = int(input())
bag = 0
while n>=0:
    if n%5 == 0:
        bag += n//5
        print(bag)
        break
    n-=3
    bag+=1
else:
    print(-1)
