
ans = 0
unique = []
for obj in objects:
    if obj not in unique:
        unique.append(obj)

print(len(unique))
