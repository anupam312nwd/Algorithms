from datetime import date, time, datetime, timedelta

some_date = date(2021, 3, 17)
print(some_date, some_date.year, some_date.month, some_date.day)
some_datetime = datetime(2021, 3, 17, 5, 23, 2)
print(some_datetime)

some_time = time(5, 23, 2)
print(some_time)

some_timedelta = timedelta(days=1, minutes=7)
new_datetime = some_datetime + some_timedelta
print(new_datetime)
