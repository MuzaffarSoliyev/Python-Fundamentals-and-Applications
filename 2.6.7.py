n = int(input())
count = 0
for i in range(1, n + 1):
    if count == n:
        break
    for _ in range(i):
        if count == n:
            break
        print(i, end=' ')
        count += 1
