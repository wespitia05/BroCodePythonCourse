import datetime

# parameters: year, month, day
date = datetime.date(2025, 1, 2)
today = datetime.date.today()

# parameters: hours, minutes, seconds
time = datetime.time(12, 30, 0)
# prints date and time of right now
now = datetime.datetime.now()

# %H = hour, %M = minutes, %S = seconds
# %m = month, %d = day, %Y = year
now = now.strftime("%H:%M:%S  %m/%d/%Y")

# future target parameters: year, month, day, hour, minute, second
target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

# have we already passed the target date?
if target_datetime < current_datetime:
    print("target date has passed")
else:
    print("target date has not passed")

print(date)
print(today)
print(time)
print(now)