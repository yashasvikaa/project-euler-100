def main():
    num = {85, 145, 42, 20, 4, 16, 37, 58}
    for i in range(2, 10000000):
        count = i
        while count != 1 and count != 39 and count not in num:
            str_count = str(count)
            count = 0
            for j in range(0, len(str_count)):
                count += int(str_count[j])**2
        if count == 39 or count in num:
            num.add(i)
    print(len(num))

if __name__ == "__main__":
    main()