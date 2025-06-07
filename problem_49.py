from itertools import permutations, combinations
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit **0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    primes = [x for x,y in enumerate(is_prime) if y]
    return primes

def main():
    primes = sieve(10000)
    primes = [p for p in primes if p > 1000]  
    primes_set = set(primes)
    visited = set()

    for p in primes:
        if p in visited:
            continue
        perms = set(int(''.join(x)) for x in permutations(str(p)) if x[0] != '0')
        prime_perms = sorted(p for p in perms if p in primes_set)
        visited.update(prime_perms)
       
        for a, b, c in combinations(prime_perms, 3):
            if b - a == c - b:
                if a != 1487 and b != 4817 and c != 8147:  
                    print(a, b, c)
                    print(f"{a}{b}{c}")
                    return  
                
if __name__ == "__main__":
    main()