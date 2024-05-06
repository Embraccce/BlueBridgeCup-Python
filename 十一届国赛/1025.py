n = int(input())
arr = list()
for i in range(n):
    si,ai,ei = map(int,input().split())
    arr.append([si+ai,ei])
arr = sorted(arr, key=lambda x: x[0] + x[1])
time_table = [arr[0][0]]
now = arr[0][0]
for idx in range(1, len(arr)):
    now += (arr[idx-1][1] + arr[idx][0])
    #print(now)
    time_table.append(now)
print(sum(time_table))

