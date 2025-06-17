from sympy import isprime

def sieve(limit):
    is_prime = [True] * (limit +1)
    is_prime[0:2] = [False, False]
    for i in range(2, limit + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    primes = [x for x, y in enumerate(is_prime) if y]
    return primes

primes_list = sieve(1_000_000)
prime_set = set(primes_list)
primes = sorted(p for p in prime_set if p not in (2, 5) and p < 10_000)

def is_concat_prime(a, b):
    return isprime(int(str(a) + str(b))) and isprime(int(str(b) + str(a)))

def build_graph():
    graph = {p: [] for p in primes}
    for i, p1 in enumerate(primes):
        graph[p1] = []
        for p2 in primes[i+1:]:
            if is_concat_prime(p1, p2):
                graph[p1].append(p2)
                graph[p2].append(p1)

    return graph

def search(graph, path, size):
    if len(path) == size:
        return path
    for candidate in graph[path[-1]]:
        if all(candidate in graph[p] for p in path):
            result = search(graph, path + [candidate], size)
            if result:
                return result
    return None

def main():
    graph = build_graph()
    for p in primes:
        print("Trying: ", p)
        result = search(graph, [p], 5)
        if result:
            print("Set: ", result)
            print("Sum: ", sum(result))
            break

if __name__ == "__main__":
    main()

