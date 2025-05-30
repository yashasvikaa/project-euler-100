def recurr(n):
    remainders = {}
    value = 1
    position = 0

    while value != 0:
        if value in remainders:
            return position - remainders[value]  # cycle length found
        remainders[value] = position
        value = (value % n) * 10
        position += 1

    return 0  # terminates if 1/n has a finite decimal


def main():
    a = 0
    b = 0
    for d in range(2,1001):
        if recurr(d) > a:
            a = recurr(d)
            b = d
    print(a)
    print(b)

if __name__ == "__main__":
    main()
    