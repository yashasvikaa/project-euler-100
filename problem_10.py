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
    sum = 0
    for i in range(0, 2000001):
        if check_prime(i):
            sum = sum + i
    print(sum)

if __name__ == "__main__":
    main()