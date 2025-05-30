# to make this considerably faster, we can skip all the a's that we have already computed (so start from 1mil-1 instead of 1 & save all the b's
# in memo = {} and proceed only for a not in memo.

def main():
    max_chain = 1
    max_num = 1
    for a in range(1,1000000):
        chain = 1
        b = a 
        while (b != 1):
            if (b% 2 ==0):
                b = b/2
                chain += 1
            else:
                b = 3*b + 1
                chain += 1
        if (chain >= max_chain):
            max_chain = chain
            max_num = a
    print(max_chain, max_num)


if __name__ == "__main__":
    main()

