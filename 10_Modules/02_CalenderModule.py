import calendar

cal = calendar.month(2025,8)
print(cal)

calendar.isleap(2024)  # This will return True, as 2024 is a leap year.
calendar.isleap(2025) # This will return False, as 2025 is not a leap year.
dir(calendar)  # This will list all the attributes and methods of the calendar module.
calendar.month_name[8]  # This will return 'August', the name of the month for index 8.
print(calendar.weekday(2025, 7, 29 ))  # This will return the day of the week for July 29, 2025, where Monday is 0 and Sunday is 6.
