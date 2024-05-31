from collections import deque

class MonotonicQueue:
    def __init__(self,compare):
        self.compare = compare
        self.mp = deque()
    def push(self,value):
        while self.mp and self.compare(self.mp[-1],value):
            self.mp.pop()
        self.mp.append(value)
    def front(self):
        return self.mp[0]
    def pop(self,value):
        if self.mp and self.mp[0] == value:
            self.mp.popleft()

n,k = map(int,input().split())
nums = list(map(int,input().split()))
def solve(compare):
    mq = MonotonicQueue(compare)
    ret = []
    for i in range(len(nums)):
        if i>=k:
            mq.pop(nums[i-k])
        mq.push(nums[i])
        if i >= k-1:
            ret.append(mq.front())
    return ret
print(*solve(lambda x,y:x>y))
print(*solve(lambda x,y:x<y))
