def solutions(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

def solution(sizes):
    answer = 0
    w = []
    h = []
    for i in sizes:
        w.append(max(i))
        h.append(min(i))
    return min(w) * max(h)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))