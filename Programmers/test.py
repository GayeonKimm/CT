def solution(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            s = s[:i] + s[i+1:]

    if len(s) == 0:
        return 1
    else:
        return 0

print(solution('baabaa'))
# 이 방법으로는 안되나.....????