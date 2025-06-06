from math import sqrt

def is_pentagonal(x):
    n = (1 + sqrt(24 * x + 1)) / 6
    return n.is_integer()

def pentagonal_numbers(n):
    return [(i * (3 * i - 1)) // 2 for i in range(1, n + 1)]

def main():
    limit = 3000  
    pent_nums = pentagonal_numbers(limit)

    min_diff = float('inf')
    for j in range(len(pent_nums)):
        for k in range(j):
            pj = pent_nums[j]
            pk = pent_nums[k]
            if is_pentagonal(pj + pk) and is_pentagonal(pj - pk):
                diff = pj - pk
                if diff < min_diff:
                    min_diff = diff
    print(min_diff)

if __name__ == "__main__":
    main()