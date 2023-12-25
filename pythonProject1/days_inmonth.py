def leap_check(year):
    if year % 4 ==0:
        if year % 100 ==0:
            if year % 400 == 0:
                return "leap"
            else:
                return "non leap"
        else:
            return "leap"
    else:
        return "non leap"


def days_in_month(month,year):
    if month == 'jan':
        return 31
    elif month == 'feb':
        re = leap_check(year)
        if re == 'leap':
            return 29
        else:
            return 28
    elif month == 'mar':
        return 31
    elif month == 'apr':
        return 30
    elif month == 'may':
        return 31
    elif month == 'jun':
        return 30
    elif month == 'jul':
        return 31
    elif month == 'aug':
        return 31
    elif month == 'sep':
        return 30
    elif month == 'oct':
        return 31
    elif month == 'nov':
        return 30
    elif month == 'dec':
        return 31
year = int(input("enter the year: "))
month = input("enter month: ").lower()
month = month[0:4]
print(f"no of days in year = {year} and month = {month} is {days_in_month(month,year)}")