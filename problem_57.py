def denom():
    frac = [2, 5]
    for i in range(2, 1000):
        frac.append(frac[i-1]*2 + frac[i-2])
    return frac
def num():
    frac_denom = denom()
    frac = [3, 7]
    for i in range(2, 1000):
        frac.append(frac_denom[i] + frac_denom[i-1])
    return frac
def main():
    count = 0
    frac_denom = denom()
    frac_num = num()
    for i in range(0, 1000):
        if len(str(frac_num[i])) > len(str(frac_denom[i])):
            count += 1
    print(count)
    

if __name__ == "__main__":
    main()