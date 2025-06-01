def convert(n):
    if n > 1:
        convert(n//2)
    
    
    
def main():
    list_case1 = []
    for i in range(0, 1000001):
        str_num = str(i)
        if str_num == str_num[::-1]:
            list_case1.append(i)
    sum = 0
    for num in list_case1:
        bin_num = bin(num)[2:]
        if bin_num == bin_num[::-1]:
            sum += num

    print(sum)

    

if __name__ == "__main__":
    main()