import calendar


month, day, year = map(int, input().split())

weekdays = [
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY"
]

day_index = calendar.weekday(year, month, day)

print(weekdays[day_index])