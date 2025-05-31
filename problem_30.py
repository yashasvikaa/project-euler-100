def main():
    n = 1
    sum = 0
    while True:
        if(n*pow(9,5) < pow(10, n-1)):
            break
        else:
            n += 1
    
    for i in range(10, pow(10,6) + 1):
        str_num = str(i)
        a = 0
        for j in str_num:
            a += pow(int(j),5)
        if(a == i):
            sum += i
    print(sum)


if __name__ == "__main__":
    main()