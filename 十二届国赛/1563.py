f = [float('inf') for i in range(1+2021)]
f[0] = 0
f[1] = 1
for i in range(2,2021+1):
    for left in range(i):
        right = i - left - 1
        f[i] = min(f[i],1+2*f[left]+3*f[right]+right*left**2)
print(f[2021])
