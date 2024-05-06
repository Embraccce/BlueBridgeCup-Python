arr = []
for i in range(300):
    temp = input()
    arr.append(temp)

trans = [''.join(t) for t in zip(*arr)]
ans = 0
for row in arr:
    for idx in range(300):
        if row[idx:idx+4] == "2020":
            ans += 1

for col in trans:
    for idx in range(300):
        if col[idx:idx+4] == "2020":
            ans += 1

for x in range(300):
    for y in range(300):
        if x + 3 < 300 and y + 3 < 300:
            if arr[x][y] == "2" and arr[x+1][y+1] == "0" and arr[x+2][y+2] == "2" and arr[x+3][y+3] == "0":
                ans += 1
print(ans)
