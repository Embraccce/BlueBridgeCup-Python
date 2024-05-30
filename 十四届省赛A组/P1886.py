from collections import deque

class MonotonicQueue:
    def __init__(self, compare):
        self.mp = deque()
        self.compare = compare
    def push(self, value):
        while self.mp and self.compare(self.mp[-1], value):
            self.mp.pop()
        # 添加进来
        self.mp.append(value)
    
    def front(self):
        return self.mp[0]
    
    def pop(self, value):
        # 仅在要移除的值是队列头部时才进行实际移除
        if self.mp and self.mp[0] == value:
            self.mp.popleft()


n,k = map(int,input().split())
nums = list(map(int,input().split()))
def solve(compare):
    mq = MonotonicQueue(compare)
    ret = []
    for i in range(len(nums)):
        # 移除生命周期到了的队头元素
        if i >= k: # 才有可能要移除
            mq.pop(nums[i-k])
        # 加入单调队列
        mq.push(nums[i])
        if i >= k - 1:
            ret.append(mq.front())
    return ret

print(*solve(lambda x,y:x>y))
print(*solve(lambda x,y:x<y))


        
        
