def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, limit + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    primes = set(x for x,y in enumerate(is_prime) if y)
    return primes


def rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def main():
    primes = set(sieve(1000000))
    check = set()
    for p in primes:
        if p not in check and all(rotation in primes for rotation in rotations(p)):
            check.update(rotations(p))
    print(len(check))


if __name__ == "__main__":
    main()