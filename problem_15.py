def single_word(n):
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    else: 
        return ""
    
def double_word(n):
    if n == 2:
        return "twenty"
    elif n == 3:
        return "thirty"
    elif n == 4:
        return "forty"
    elif n == 5:
        return "fifty"
    elif n == 6:
        return "sixty"
    elif n == 7:
        return "seventy"
    elif n == 8:
        return "eighty"
    elif n == 9:
        return "ninety"
    else:
        return ""
    
def double_word_w_zero(n):
    if n == 11:
        return "eleven"
    elif n == 12:
        return "twelve"
    elif n == 13:
        return "thirteen"
    elif n == 14:
        return "fourteen"
    elif n == 15:
        return "fifteen"
    elif n == 16:
        return "sixteen"
    elif n == 17:
        return "seventeen"
    elif n == 18:
        return "eighteen"
    elif n == 19:
        return "nineteen"
    else:
        return "ten"
    

def num_to_words(n):
    str = ""
    if n < 10:
        str += single_word(n)
    elif n < 100:
        if n//10 == 1:
            str += double_word_w_zero(n)
        else:
            str += double_word(n//10)
            str += single_word(n%10)
    elif n < 1000:
         str += single_word(n//100) 
         str += "hundred"
         if (n%100 != 0):
            str += "and"
            str += num_to_words(n%100)
    else:
        str = "onethousand"
    return str

def main():
    sum = 0 
    for i in range(1, 1001):
        sum += len(num_to_words(i))
    print(sum)

if __name__ == "__main__":
    main()