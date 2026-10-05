###datetime for today

from datetime import date
today = date.today()

print(today)

###current date (year, month, day)
from datetime import date

today = date.today()

print(today.year)
print(today.month)
print(today.day)

###specific date create
from datetime import date

birthday = date(2002, 12, 16)

print(birthday)

##### two date compare
from datetime import date

date1 = date(2026, 10, 5)
date2 = date(2026, 12, 25)

print(date1 < date2)

#####two date difference 
from datetime import date

date1 = date(2026, 10, 5)
date2 = date(2026, 10, 15)

difference = date2 - date1

print(difference)
print(difference.days)

####timedelta (date + day)
from datetime import date, timedelta

today = date.today()

future_date = today + timedelta(days=7)

print(future_date)

#####(date - day)
from datetime import date, timedelta

today = date.today()

previous_date = today - timedelta(days=7)

print(previous_date)

###month/year
from datetime import date

my_date = date(2026, 10, 5)

print(my_date.year)
print(my_date.month)
print(my_date.day)

####current time
from datetime import datetime

now = datetime.now()

print(now)

####Current Hour, Minute, Second
from datetime import datetime

now = datetime.now()

print(now.hour)
print(now.minute)
print(now.second)

####date format change
from datetime import date

today = date.today()

print(today.strftime("%d-%m-%Y"))
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%B %d, %Y"))

####strptime()___string to date
from datetime import datetime

date_string = "21-03-2001"

my_date = datetime.strptime(date_string, "%d-%m-%Y")

print(my_date)


####practice 1

from datetime import date, timedelta

# Get today's date
today = date.today()

# Calculate future and previous dates
future_date = today + timedelta(days=7)
previous_date = today - timedelta(days=7)

# Display dates
print("Today:", today.strftime("%d-%m-%Y"))
print("After 7 days:", future_date.strftime("%d-%m-%Y"))
print("Before 7 days:", previous_date.strftime("%d-%m-%Y"))
