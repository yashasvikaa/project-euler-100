from sympy import isprime

def main():
    total_diagonals = 1
    prime_diagonals = 0
    side_length = 1
    current = 1

    while True:
        side_length += 2
        step = side_length - 1

        # Generate the 3 diagonal corners (top-right is skipped; always a square)
        for _ in range(3):
            current += step
            if isprime(current):
                prime_diagonals += 1

        # bottom-right corner (just to move to the next layer)
        current += step

        total_diagonals += 4
        ratio = prime_diagonals / total_diagonals

        if ratio < 0.10:
            print(side_length)
            break

if __name__ == "__main__":
    main()