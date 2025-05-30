def read_name():
    with open("problem_22(ques).txt", "r") as file:
        contents = file.read()
        names = contents.replace('"',''). split(',')
        names.sort()
    return names

def name_score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

def main():
    sum = 0
    names = read_name()
    for i, name in enumerate(names, start = 1):
        sum += name_score(name) * i
    print(sum)



if __name__ == "__main__":
    main()