from math import isqrt
def reader():
    with open("problem_42(ques).txt", "r") as file:
        content = file.read()
    words = content.replace('"', '').split(',')
    return words

def value(word):
    val = sum(ord(char) - ord('A') + 1 for char in word)
    return val

def isTriangular(num):
    new_num = 2*num
    n = isqrt(new_num)
    if n*(n+1) == new_num:
        return True
    else: 
        return False

def main():
    words = reader()
    values = [value(word) for word in words]
    sum = 0
    for val in values:
        if isTriangular(val):
            sum += 1
    print(sum)

if __name__ == "__main__":
    main()