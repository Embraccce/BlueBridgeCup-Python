n = int(input())
time = 0
def get_bit_sum(num):
    tot=0
    while num:
        tot += num % 10
        num //= 10
    return tot
while get_bit_sum(n) != 0:
    n-=get_bit_sum(n)
    time += 1
print(time)
