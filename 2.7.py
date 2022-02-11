s = input()

cur = ''
length = 0
res = ''
for i in s:
    if i != cur:
        res += cur
        cur = i
        if length != 0:
            res += str(length)
            length = 0
        length = 1
    else:
        length += 1
res += cur
res += str(length)
print(res)
