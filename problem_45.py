from math import sqrt

def is_pentagonal(x):
    n = (1 + sqrt(24 * x + 1)) / 6
    return n.is_integer()

def main():
    n = 144  
    while True:
        hex_num = n * (2 * n - 1)
        if is_pentagonal(hex_num):
            print(hex_num)
            break
        n += 1

if __name__ == "__main__":
    main()
