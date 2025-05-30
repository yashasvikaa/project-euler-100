import math

def squared(n):
    sum = 0
    for i in range(1, n+1):
        sum += pow(i, 2)
    return sum

def square(n):
    sum = 0
    for i in range(1, n+1):
        sum += + i
    return pow(sum, 2)

def main():
    print(squared(100) - square(100))

if __name__ == "__main__":
    main()