def make_str():
    num_str  = "123456789"
    i = 9
    num = 1
    while (i < 999991):
        for j in range(0, 10):
            num_str += str(num) + str(j)
        i += 10 + 10*len(str(num))
        num += 1
    return num_str

def main():
    num_str = make_str()
    product = 1
    i = 1
    while(i < 1000000):
        product = product*int(num_str[i-1])
        i = i*10
    print(product)

if __name__ == "__main__":
    main()