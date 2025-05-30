def days_in_year(n):
    if (n%4 == 0):
        if (n%100 == 0) and (n%400 != 0):
            return 365
        return 366
    else:
        return 365
    
def days_in_month(month, year):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        return 31
    elif(month == 4) or (month == 6) or (month == 9) or (month == 11):
        return 30
    else: 
        if(days_in_year(year) == 365):
            return 28
        else:
            return 29

    
def sunday(date, month, year):
    sum = 0
    for i in range(1900,year):
        sum += days_in_year(i)
    for j in range(1,month):
        sum += days_in_month(j, year)
    for k in range(1, date+1):
        sum += 1
    if (sum%7 == 0):
        return True
    else:
        return False
         

def main():
    sum = 0
    date = 1
    for year in range(1901,2001):
        for month in range(1,13):
            if(sunday(date, month, year)):
                sum+= 1

    print(sum)

if __name__ == "__main__":
    main()