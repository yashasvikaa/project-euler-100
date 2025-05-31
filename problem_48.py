import math
def main():
    sum = 0 
    for i in range(1, 1001):
        sum += pow(i, i)%10000000000
    str_num = str(sum)
    print(str_num[len(str_num)-10:len(str_num)])

if __name__ == "__main__":
    main()