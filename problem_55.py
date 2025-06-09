def check(n):
    i = 0
    while i < 50:
        str_num = str(n)
        n += int(str_num[::-1])
        str_num = str(n)
        if str_num == str_num[::-1]:
            return True
        i += 1  
    return False
        
def main():
    num = 0
    for i in range(1, 10001):
        if not check(i):
            num += 1
    print(num)

if __name__ == "__main__":
    main()