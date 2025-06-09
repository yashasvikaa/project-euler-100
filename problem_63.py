def main():
    count = 0
    n = 1
    while len(str(9**n)) >= n:
        for x in range(1, 10):
            if len(str(x**n)) == n:
                count += 1
        n += 1
    print(count)

if __name__ == "__main__":
    main()