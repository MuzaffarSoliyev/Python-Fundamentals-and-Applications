n = int(input())

CLASSES = {}

for i in range(n):
    line = input().split(':')
    if len(line) > 1:
        for parent in line[1].strip().split():
            CLASSES[parent].append(line[0].strip())
        if line[0].strip() not in CLASSES.keys():
            CLASSES[line[0].strip()] = []
    else:
        CLASSES[line[0].strip()] = []

n = int(input())
for i in range(n):
    parent, child = input().split()
    if child in CLASSES[parent]:
        print('Yes')
    else:
        print('No')
