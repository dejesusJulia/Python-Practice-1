# Example Files for working with Calendars

# import calendar module
import calendar

"""""
Create a plain text calendar
"""""
# c = calendar.TextCalendar(calendar.MONDAY)
# st = c.formatmonth(2023, 1, 0, 0)
# print(st)

# Create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2023, 1)
# print(st)

# loop over days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in hc.itermonthdays(2023,8) :
#     print(i)

''''
The Calendar module provides useful utilities for the given locale, usch as the names of days and months in both full and abbreviated forms
'''
# for name in calendar.month_name: 
#     print(name)

# for day in calendar.day_name: 
#     print(day)

''''
Calculate days based on a rule. For example, consider a team meeting on the first Fridat of every month. To figure out what days that would be for each month, we can use this script: 
'''
print("Team Meetings will be on: ")
for m in range(1,13): 
    cal = calendar.monthcalendar(2023, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0: 
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    
    print("%10s %2d" % (calendar.month_name[m], meetday))