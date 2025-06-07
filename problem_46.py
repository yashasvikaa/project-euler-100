def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
         if is_prime[i]:
             for j in range(i * i, limit + 1, i):
                 is_prime[j] = False
    primes = [x for x,y in enumerate(is_prime) if y]
    return primes

def main():
    limit = 1000000
    primes = sieve(limit)
    primes_set = set(primes)
    n = 9
    while n < limit:
        if n not in primes_set:  # odd composite
            can_be_written = False
            for p in range(1, int(n**0.5)):
                t = n - 2*p*p 
                if t <= 0:
                    break
                if t in primes_set:
                    can_be_written = True
                    break
            if not can_be_written:
                print(n)
                break
        n += 2

if __name__ == "__main__":
    main()