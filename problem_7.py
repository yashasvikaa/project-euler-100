def check_prime(n):
    if (n < 2):
        return False
    a = 2
    while (a*a <= n):
        if(n%a ==0):
            return False
        a += 1
    return True

def main():
    a = 0
    num = 2
    while (a < 10001):
        if(check_prime(num)):
            a += 1
        num += 1
    print(num-1, a)

if __name__ == "__main__":
    main()