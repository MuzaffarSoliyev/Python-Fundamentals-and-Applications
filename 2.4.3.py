string = input().lower()
count = 0
for i in string:
    if i == 'c' or i == 'g':
        count += 1

print(count / len(string) * 100)

