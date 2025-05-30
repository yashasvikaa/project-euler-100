def main():
    max_pal = 0
    
    for a in range(999,99,-1):
        for b in range(999,99,-1):
            product = a*b
            if str(product) == str(product)[::-1]:
                if product > max_pal:
                    max_pal = product
    print(max_pal)
if __name__ == "__main__":
    main()