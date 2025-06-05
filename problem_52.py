def main():
    num = 1
    while True:
        sorted_digits = sorted(str(num))
        if all(sorted(str(num * i)) == sorted_digits for i in range(2, 7)):
            print(num)
            return
        num += 1

if __name__ == "__main__":
    main()