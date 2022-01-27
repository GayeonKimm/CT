import sys
input = sys.stdin.readline

s = list(map(str, input().strip()))
t = list(map(str, input().strip()))

# pop 하려면 str여야 한대

while len(t) != len(s):
    if t[-1] == 'B':
        t.pop()
        t = t[::-1]
        # t.reverse()
    else:
        t.pop()

if t == s:
    print(1)
else:
    print(0)