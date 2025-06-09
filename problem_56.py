def main():
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            str_num = str(pow(a,b))
            total = sum(int(element) for element in str_num)
            if total > max_sum:
                max_sum = total
    print(max_sum)

if __name__ == "__main__":
    main()