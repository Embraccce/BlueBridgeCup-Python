import queue
q = queue.PriorityQueue()
nums = [3,2,1,5,6,4]
k = 2
for num in nums:
    q.put(-num)
for i in range(k):
    ans = -q.get()
