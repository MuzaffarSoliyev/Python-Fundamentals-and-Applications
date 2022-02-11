a = int(input())
b = int(input())

mul = a * b

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(int(mul / a))
