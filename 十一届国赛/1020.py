import math
def is_prime(num):
    if num<=1:
        return False
    if num==2:
        return True
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i ==0:
            return False
    return True
primes = []
for num in range(1,101):
    if is_prime(num):
        primes.append(num)
        
print(primes)
nums = dict()
for num in primes:
    nums[num] = 0

for i in range(2,101):
    now = i
    while now != 1:  
        for prime in range(1,101):
            if prime in primes and now % prime == 0:
                now //= prime
                nums[prime] += 1
                break
ans  = 1
for value in nums.values():
    ans *= (value + 1)
print(ans)
    
    
