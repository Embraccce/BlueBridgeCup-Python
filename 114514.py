import datetime

start = datetime.date(2000, 1, 1)
end = datetime.date(2020, 10, 1)
days = datetime.timedelta(days=1)
ans = 0

while end >= start:
    if start.day == 1 or start.weekday() == 0:
        ans += 2
    else:
        ans += 1
    start += days
print(ans)
