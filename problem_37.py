from math import isqrt
def prime(n):
    if n < 2:
        return False
    sqrt = isqrt(n)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    str_num = str(n)
    for i in range(0, len(str_num)):
        if not prime(int(str_num[i:len(str_num)])):
            return False
        if not prime(int(str_num[0:len(str_num)-i])):
            return False
    return True


def main():
    num = 0
    sum = 0
    a = 11
    while (num < 11):
        if check(a):
            num += 1
            sum += a
        a += 1
    print(sum)

if __name__ == "__main__":
    main()