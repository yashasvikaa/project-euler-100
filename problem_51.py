from itertools import combinations

def sieve(limit):
    # use a sieve function (and a set lookup) for a O(1) lookup instead of O(n)
    is_prime = [True]*(limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, limit+1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False
    primes = [x for x, y in enumerate(is_prime) if (y and len(str(x)) >= 6)]
    return primes

def main():
    primes = sieve(1000000)
    primes_set = set(primes)
    # not possible by replacing 2 digits (trial and error conclusion)
    for prime in primes:
        str_p = str(prime)
        for d in '0123456789':
            indices = [i for i, ch in enumerate(str_p) if ch == d]
            if len(indices) < 3: 
                continue  # not enough positions to form a family of size 8 (i.e. not possible by replacing 2 digits)

            # try all subsets of indices (size 1 to len(indices))
            for r in range(1, len(indices) + 1):
                for positions in combinations(indices, r):
                    family = []
                    for repl_digit in '0123456789':
                        temp = list(str_p)
                        for pos in positions:
                            temp[pos] = repl_digit
                        candidate = int(''.join(temp))
                        # Skip numbers with leading zero
                        if len(str(candidate)) != len(str_p):
                            continue
                        if candidate in primes_set:
                            family.append(candidate)
                    if len(family) == 8:
                        print(f"Found family: {family}")
                        print(f"Smallest prime: {min(family)}")
                        return


if __name__ == "__main__":
    main()