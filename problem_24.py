from itertools import permutations

def main():
    perms = permutations('0123456789')
    for i, p in enumerate(perms):
        if i == 999999:
            print(''.join(p))
       

if __name__ == "__main__":
    main()