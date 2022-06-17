'''
try - except 구문 사용!!

'''
while True:
    try:
        n = input()
        print(n)
    except EOFError:
        break
