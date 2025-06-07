def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit **0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [x for x,y in enumerate(is_prime) if y]
    return primes

def main():
    primes = sieve(999999)
    primes_set = set(primes)
    loops = 0 
    largest_sum = 0
    for i in range(0, len(primes)):
        sum = 0
        for j in range(i, len(primes)):
            sum += primes[j]
            if sum >= 999999:
                break
            if sum in primes_set and j - i + 1 > loops:
                largest_sum = sum
                loops = j - i + 1
    print(largest_sum, loops)

if __name__ == "__main__":
    main()