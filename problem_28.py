def main():
    sum_left = 0
    sum_right = 0
    right_a = 1
    left_a = 1
    left_b = 2
    right_b = 4
    for left_i in range(1,1001):
        left_a = left_a + left_b
        left_b += 2
        sum_left += left_a
    for right_i in range(1,1001):
        right_a = right_a + right_b
        if(right_i%2 == 0):
            right_b += 4
        sum_right += right_a
    
    print(sum_left + sum_right + 1)

if __name__ == "__main__":
    main()