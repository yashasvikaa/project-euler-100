def main():
    
    digit_facs = [1]  
    for i in range(1, 10):
        digit_facs.append(digit_facs[-1] * i)

    total = 0
    for i in range(10, 7 * digit_facs[9]):  
        sum_digits = sum(digit_facs[int(d)] for d in str(i))
        if sum_digits == i:
            total += i

    print(total)

if __name__ == "__main__":
    main()