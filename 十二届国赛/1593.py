def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count
N, K = map(int,input().split())
ans = 0
num = 1
while num <= N:
    if count_set_bits(num) == K:
        ans += 1
    num += 1
print(ans)
