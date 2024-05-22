from datetime import datetime
data = []
with open('records.txt','r') as file:
    for line in file:
        data.append(datetime.strptime(line.strip(), "%Y-%m-%d %H:%M:%S"))
data.sort()
ans = 0
for i in range(0,len(data),2):
    delta = data[i+1] - data[i]
    ans += int(delta.total_seconds())
print(ans)


