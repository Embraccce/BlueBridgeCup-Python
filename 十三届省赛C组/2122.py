n = int(input())
m = int(input())
def sum_of_digits(n):
    tot = 0
    while n:
        tot += n % 10
        n //= 10
    return tot
arr = sorted(range(1,n+1),key=sum_of_digits)
print(arr[m-1])
