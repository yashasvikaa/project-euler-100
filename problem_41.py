from itertools import permutations
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def main():
    for n in range(7,0,-1):
        digits = ''.join(str(i) for i in range(1, n+1))
        for p in sorted(permutations(digits), reverse = True):
            num = int(''.join(p))
            if is_prime(num):
                print(num)
                return
    

if __name__ == "__main__":
    main()
