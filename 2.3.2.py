a = int(input())
b = int(input())
c = int(input())
d = int(input())

for j in range(c, d + 2):
    if j == c:
        print(" ", end='\t')
    else:
        print(j - 1, end='\t')
print()
for i in range(a, b + 1):
    for j in range(c, d + 1):
        if j == c:
            print(i, i * j, sep='\t', end='\t')
        else:
            print(i * j, sep='\t', end='\t')
    print()
