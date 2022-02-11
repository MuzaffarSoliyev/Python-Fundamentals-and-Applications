n = int(input())

if n % 10 == 0 or n % 10 == 5 or \
        n % 10 == 6 or n % 10 == 7 or \
        n % 10 == 8 or n % 10 == 9 or \
        n % 100 == 11 or n % 100 == 12 or \
        n % 100 == 13 or n % 100 == 14:
    print(n, 'программистов')
elif n % 10 == 1:
    print(n, 'программист')
else:
    print(n, 'программиста')
