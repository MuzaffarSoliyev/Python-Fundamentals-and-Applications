s = input()
a = input()
b = input()

count = 0
while a in s:
    s = s.replace(a, b)
    count += 1
    if count > 1000:
        print('Impossible')
        break
if count <= 1000:
    print(count)
