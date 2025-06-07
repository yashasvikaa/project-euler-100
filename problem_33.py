def new_frac(num, denom):
    str_num = str(num)
    str_denom = str(denom)
    new_num = ''
    new_denom = ''
    for i in range(0, 2):
        for j in range(0, 2):
            if str_num[i] == str_denom[j] and int(str_num[i]) != 0:
                new_num = str_num.replace(str_num[i],'')
                new_denom = str_denom.replace(str_num[i], '')
    if len(new_num) == 1 and len(new_denom) == 1:
        if int(new_num) != 0 and int(new_denom) != 0 and int(new_num) < int(new_denom):
            return int(new_num), int(new_denom)
    return 1, 1

def main():
    grid = []
    for num in range(10, 100):
        for denom in range(num + 1, 100):
            new_num, new_denom = new_frac(num, denom)
            if new_num/new_denom == num/denom:
                grid.append((new_num, new_denom))
    print(grid)

if __name__ == "__main__":
    main()