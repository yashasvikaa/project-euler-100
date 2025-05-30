import math

def sum_of_div(n):
    sum = 0
    for a in range(1, math.isqrt(n)+1):
        if (n%a == 0):
            sum += a
            if (n//a != a):
                sum += n//a

    return (sum - n)

def abundant_num(n):
    return(sum_of_div(n) > n)

def main():
    limit = 28123
    abun_list = [i for i in range(1, limit + 1) if abundant_num(i)]
    can_be_written = [False] * (limit + 1)
    for i in range(0, len(abun_list)):
        for j in range(i, len(abun_list)):
            ab_sum = abun_list[i] + abun_list[j]
            if ab_sum <= limit:
                can_be_written[ab_sum] = True
            else:
                break
    print(sum(i for i in range(1, limit+1) if not can_be_written[i]))

if __name__ == "__main__":
    main()