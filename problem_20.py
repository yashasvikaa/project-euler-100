def fac(n):
    if n == 1:
        return 1
    else: 
        return n*fac(n-1)

def sum(n):
    str_num = str(n)
    sum = 0
    for i in range (0, len(str_num)):
        sum += int(str_num[i])
    return sum

def main():
    print(sum(fac(100)))
if __name__ == "__main__":
    main()