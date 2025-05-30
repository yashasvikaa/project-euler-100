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
    n = 2
    num = 2
    while n*n <= 600851475143:
        if 600851475143%n ==0:
            if(check_prime(n)) & (n>num):
                num = n
                
        n +=1
    print(num)
    
if __name__ == "__main__":
    main()