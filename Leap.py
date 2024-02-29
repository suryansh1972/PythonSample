month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 23] #This is a list

def is_leap(year):
    return year % 4 == 0 &  (year % 100 != 0 | year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year"""

    if not 1 <= month <= 12:
        return'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2017, 2))