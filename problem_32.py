from math import isqrt
def divisors(n):
    grid = []
    for i in range(1, isqrt(n) + 1):
        if n%i == 0:
            grid.append((i, n//i))
    return grid

def isPandigit(num1, num2, num3):
    str_num = str(num1) + str(num2) + str(num3)
    for i in range(1, 10):
        if str(i) not in str_num:
            return False
    return True


def main():
    pandigits = []
    for num in range(1, 9999):
        grid = divisors(num)
        for (a,b) in grid:
            if isPandigit(a,b,num):
                if num not in pandigits:
                    pandigits.append((num))
    print(sum(p for p in pandigits))



if __name__ == "__main__":
    main()