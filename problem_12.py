def divisors(n):
    sum = 0
    for i in range(1, n+1):
        if n%i == 0:
            sum += 1
    return sum

def main():
    n = 1
    a = 1
    while (divisors(a) < 500):
        n += 1
        a = (n*(n+1))//2
    print(a)
        
    

if __name__ == "__main__":
    main()