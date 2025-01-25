import datetime

now = datetime.datetime.now()

month = now.month
day = now.day
minute = now.minute
second = now.second

print("Current Month:", month)
print("Current Day:", day)
print("Current Minute:", minute)
print("Current Second:", second)



now = datetime.datetime.now()


year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

print(f"Current Date and Time: {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}")