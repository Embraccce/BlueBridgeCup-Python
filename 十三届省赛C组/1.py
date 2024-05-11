import math
lst=[]
n=2
for i in range(1,math.ceil(math.sqrt(n))):
    if n % i == 0:
        lst.append(i)
        lst.append(n//i)
print(lst)
