fac = [1, 1]
for i in range(2, 101):
    fac.append(i*fac[i-1])

def comb(n, r):
    denom = fac[r]*fac[n-r]
    val = fac[n]//denom
    return val

def main():
    num = 0
    for n in range(1, 101):
        for r in range(0, n//2):
            if comb(n,r) > 1000000:
                num += 2*(n//2 - r) 
                if n%2 ==0:
                    num += 1
                else:
                    num += 2
                break
    print(num)
    
if __name__ == "__main__":
    main()