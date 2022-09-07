
# ## 💻 Exercises: Day 16
from datetime import date, datetime

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)
# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S"
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)
# 3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)
# 4. Calculate the time difference between now and new year.
today = date(year=2022, month=9, day=7)
new_year = date(year=2023, month=1, day=1)
til_new_year = new_year - today
print(til_new_year)
# 5. Calculate the time difference between 1 January 1970 and now.
jan_1_1970 = date(year=1970, month=1, day=1)
since_jan_1970 = today - jan_1_1970
print(since_jan_1970)
# 6. Think, what can you use the datetime module for? Examples:
#    - Time series analysis
#    - To get a timestamp of any activities in an application
#    - Adding posts on a blog 

# 🎉 CONGRATULATIONS ! 🎉
