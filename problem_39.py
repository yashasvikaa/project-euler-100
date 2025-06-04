def solution(p):
    count = 0
    for a in range(1, p // 3):
        for b in range(a, (p - a) // 2):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count
            
def main():
    max_sol = 0
    num = 3
    for p in range (3, 1001):
        if solution(p) > max_sol:
            max_sol = solution(p)
            num = p
    print(num, max_sol)

if __name__ == "__main__":
    main()