def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [x for x, y in enumerate(is_prime) if y]

primes = sieve(100000)

def count_distinct_prime_factors(n):
    count = 0
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            count += 1
            while n % p == 0:
                n //= p
    if n > 1:
        count += 1  
    return count

def main():
    i = 1
    while True:
        if all(count_distinct_prime_factors(i + k) == 4 for k in range(0, 4)):
            print(i)
            break
        i += 1

if __name__ == "__main__":
    main()