def product(num):
    str_num = ''
    i = 1
    while len(str_num) < 9:
        str_num += str(num*i)
        i += 1
    if len(str_num) == 9 and set(str_num) == set('123456789'):
        return int(str_num)
    else:
        return 0

def main():
    largest_pan = 0
    for i in range(1, 10000):
        j = product(i)
        if j > largest_pan:
            largest_pan = j
    print(largest_pan)


if __name__ == "__main__":
    main()