import math
def main():
    str_num = str(pow(2,1000))
    sum = 0
    for i in range(0, len(str_num)):
        sum += int(str_num[i])
    print(sum)

if __name__ == "__main__":
    main()
