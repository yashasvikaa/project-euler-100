from itertools import product

def reader():
    with open("problem_59(ques).txt") as f:
        encrypted = list(map(int, f.read().split(",")))
    return encrypted

def is_acceptable(char):
    if char < 32:
        return False
    elif char > 122:
        return False
    elif 60 <= char <= 62:
        return False
    elif char == 64 or char == 42:
        return False
    elif 36 <= char <= 38:
        return False
    else:
        return True

def main():
    encrypted = reader()
    iteration = 0
    for key in product(range(ord('a'), ord('z') + 1), repeat = 3):
        iteration += 1
        decrypted = []
        for i, val in enumerate(encrypted):
            decrypted_val = val ^ key[i % 3]
            if not is_acceptable(decrypted_val):
                break
            decrypted.append(decrypted_val)
        else:
            text = ''.join(map(chr, decrypted))
            print("Decrypted Message: ", text)
            print("\nKey: ", ''.join(map(chr, key)))
            print("Sum of ASCII values: ", sum(decrypted))
            print("Iteration number: ", iteration)
        


if __name__ == "__main__":
    main()