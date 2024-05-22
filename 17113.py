from datetime import datetime,timedelta
ans = 0
now = datetime(2023,1,1)
end = datetime(2023,12,31)
d = timedelta(days=1)
while now <= end:
    month = str(now.month)
    day = str(now.day)
    week = str(now.weekday()+1)
    if '1' in month or '1' in day or '1' in week:
        ans+=5
    else:
        ans += 1
    now += d
print(ans)
