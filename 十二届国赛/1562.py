import datetime
arr = []
for i in range(1000):
    arr.append(i**2)

start = datetime.datetime(2001,1,1)
end = datetime.datetime(2021,12,31)
delta = datetime.timedelta(days=1)
ans = 0
while start <= end:
    if sum(map(lambda x: int(x), start.strftime("%Y%m%d"))) in arr:
        ans+=1
    start += delta
print(ans)
