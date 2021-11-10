# 뭔소리지? 했는데 풀었음
c = int(input())
for i in range(c):
    h, w, n = map(int, input().split())
    if n % h == 0:
        n_ho = n//h
        n_th = h
    else:
        n_ho = n//h+1
        n_th = n%h
    print(n_th*100 + n_ho)

