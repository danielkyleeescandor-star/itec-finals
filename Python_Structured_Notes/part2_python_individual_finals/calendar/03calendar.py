import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

weekday = calendar.weekday(year, month, day)

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

print("The day is:", days[weekday])