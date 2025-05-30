import math 

def sum_of_div(n):
    sum = 0
    b = math.isqrt(n)
    for a in range(1, b+1):
        if (n%a == 0):
            sum += a
            sum += n//a
            if (a == n//a):
                sum = sum - a

    return (sum - n)

def main():
    grid = []
    a = 1
    sum = 0
    for a in range(1, 10000):
        if a in grid:
            continue
        b = sum_of_div(a)
        if b <= 0 or b >= 10000:
            continue
        if b != a and sum_of_div(b) == a:
            sum += a + b
            grid.append(a)
            grid.append(b)
    print(sum)


if __name__ == "__main__":
    main()