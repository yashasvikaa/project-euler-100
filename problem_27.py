def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] == [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    primes = [x for x, prime in enumerate(is_prime) if prime]
    return primes

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main(): 
    primes = sieve(1000)
    max_prime = [0,0,0]
    for a in range(-999, 1000):
        for b in primes:
            n = 1 
            while True:
                if not isPrime(n*n + a*n + b):
                    break
                n += 1
            if n > max_prime[0]:
                max_prime[0:3] = [n, a, b]
    print(max_prime, max_prime[1]*max_prime[2])


if __name__ == "__main__":
    main()