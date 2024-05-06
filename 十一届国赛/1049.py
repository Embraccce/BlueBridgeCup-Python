import os
import sys
from collections import Counter
k = int(input())
s = input()
sub_len = len(s) // k
if len(s) % k != 0:
    print(-1)
else:
    ans = 0
    for idx in range(len(s)//k):
        d = dict(Counter(s[idx::sub_len]))
        ans += (k - max(d.values()))
    print(ans)
    
