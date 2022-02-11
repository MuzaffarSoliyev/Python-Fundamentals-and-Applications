def primes():
    a = 2
    while True:
        is_prime = False
        for i in range(2, a):
            if a % i == 0:
                is_prime = True
                break
        if not is_prime:
            yield a
        a += 1
