import math

def main():
    num = 1
    for i in range(1,21):
        num = math.lcm(num, i)
    print(num)

if __name__ == "__main__":
    main()