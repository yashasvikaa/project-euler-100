def read_grid():
    grid = []
    with open("problem_67(ques).txt", "r") as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            grid.append(row)

    return grid

def main():
    grid = read_grid()
    for i in range(len(grid) - 2,-1,-1):
        for j in range(0,i+1):
            grid[i][j] += max(grid[i+1][j], grid[i+1][j+1])
    print(grid[0])

if __name__ == "__main__":
    main()