# the variables below must be inpute from keyboard
# where 'day' 'month' and 'year' are the current
# dates of today and 'b_day' 'b_month' and 'b_year' 
# are the dates of your birthday
day = int(input("today's day: "))
month = int(input("today's month: "))
year = int(input("today's year: "))
b_day = int(input("birth day: "))
b_month = int(input("birth month: "))
b_year = int(input("birth year: "))

# 'days' is the variable that counts the days from
# birth date to current day.'copy_b_year' is a copy
# of the year of birth
days = -1
copy_b_year = b_year

if b_year % 4 == 0 :
    if b_month > 2 :
        days = days + 365
    else :
        days = days + 366
    copy_b_year = copy_b_year + 1

# checks if the year is leap year or not and adding
# to the 'days' variable the days from a whole year
for i in range(copy_b_year, year) :
    if i % 4 == 0 :
        days = days + 366
    else :
        days = days + 365
    if i % 100 == 0 :
        days = days - 1
    if i % 400 == 0 :
        days = days + 1

current_month = b_month

# checks if the b-day month is greater than the corrent
# month or not. If it is, you remove the days from the
# 'days' variable until you reach the exact month.
# does the same if the b-day month is lower than the current
# but instead of removing it's adding days
if current_month < month :
    while current_month != month :
        if current_month == 1 or 3 or 5 or 7 or 8 or 10 or 12 :
            days = days + 31
            current_month = current_month + 1
        elif current_month == 2 :
            if year % 4 == 0 :
                days = days + 29
                current_month = current_month + 1
            else :
                days = days + 28
                current_month = current_month + 1
        elif current_month == 4 or 6 or 9 or 11 :
            days = days + 30
            current_month = current_month + 1
elif current_month > month :
    while current_month != month : 
        if current_month - 1 == 1 or 3 or 5 or 7 or 8 or 10 or 12 :
            days = days - 31
            current_month = current_month - 1
        elif current_month - 1 == 2 :
            if year % 4 == 0 :
                days = days - 29
                current_month = current_month - 1
            else :
                days = days - 28
                current_month = current_month - 1
        elif current_month - 1 == 4 or 6 or 9 or 11 :
            days = days - 30
            current_month = current_month - 1

# checks if the b-day day is greater or lower than the current
# day and adds or removes the difference of days
if b_day < day :
    days = days + (day - b_day)
if b_day > day :
    days = days - (b_day - day)

# print the number of days from a birthday to the current day
print("The number of days from your birthday to the current date:", days)