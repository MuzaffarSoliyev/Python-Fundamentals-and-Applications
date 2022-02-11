s = list(map(int, input().split()))
s.sort()
cur = s[0]
count = 1
for i in range(1, len(s)):
    if s[i] == cur:
        count += 1
    else:
        if count > 1:
            print(cur)
            count = 1
        cur = s[i]

if count > 1:
    print(cur)
