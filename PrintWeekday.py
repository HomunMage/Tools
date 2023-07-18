from datetime import datetime, timedelta
import calendar

today = datetime.today()
day_from_sunday = (today.weekday() + 1) % 7
sunday = today - timedelta(day_from_sunday)

output = ""
for d in range(7):
    weekday = sunday + timedelta(days=d)    
    output += "\t" + str(weekday.month) + "/" + str(weekday.day) + "(" + calendar.day_abbr[weekday.weekday()] + ")"

print(output)

# https://www.programiz.com/python-programming/online-compiler/