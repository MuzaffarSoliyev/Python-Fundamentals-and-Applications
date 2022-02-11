lst = list(map(int, input().split()))
n = int(input())
yes = False
for i in range(len(lst)):
    if lst[i] == n:
        yes = True
        print(i, end=' ')
if not yes:
    print('Отсутствует')