import datetime
from xml.dom.expatbuilder import theDOMImplementation

# Get current date and time
datetime_object = datetime.datetime.now()
# print(datetime_object)

# Get current date
date_object = datetime.date.today()
# print(date_object)

# Date object to represent a given date
date = datetime.date(2022, 8, 24)
# print(date)

# Get components of today's date
current_date = datetime.date.today()
# print(f"Today's date is {current_date}")
# print(f"The current year is {current_date.year}")
# print(f"The current month is {current_date.month}")
# print(f"The current day of the month is {current_date.day}")

# Get date from timestamp
timestamp = datetime.date.fromtimestamp(1615059350)
# print(timestamp)

# Find the difference between two time values
t1 = datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = datetime.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
# print(t3)

# Rearrange datetime format: https://strftime.org/
local = datetime.datetime.now()
print(f"The time is {local.strftime('%-I:%M %p')} or {local.strftime('%H:%M:%S')} on {local.strftime('%A')}, {local.strftime('%d/%b/%Y')}")