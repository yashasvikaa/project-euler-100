from itertools import permutations

def check(s):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):  
        if int(s[i:i+3]) % primes[i-1] != 0:
            return False
    return True

def main():
    total = 0
    for p in permutations('0123456789'):
        s = ''.join(p)  
        if check(s):
            total += int(s)
    print(total)

if __name__ == "__main__":
    main()