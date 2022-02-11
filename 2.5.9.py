s = list(map(int, input().split()))
n = len(s)
if n > 1:
    print(s[n - 1] + s[1], end=' ')
    for i in range(1, n - 1):
        print(s[i - 1] + s[i + 1], end=' ')
    print(s[n - 2] + s[0], end=' ')
else:
    print(s[0])
    