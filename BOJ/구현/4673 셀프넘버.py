numbers = set(range(1, 10001))
gener_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    gener_num.add(i)

self_num = sorted(numbers - gener_num)
for i in self_num:
    print(i)
