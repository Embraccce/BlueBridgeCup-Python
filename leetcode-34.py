nums = [5,7,7,8,8,10]
target = 6
l,r=-1,len(nums)
while l+1!=r:
    m = l+r>>1
    if nums[m]<target:
        l = m
    else:
        r = m
if nums[r] == target:
    ans = [r]
else:
    ans = [-1]
l,r=-1,len(nums)
while l+1!=r:
    m = l+r>>1
    if nums[m]<=target:
        l = m
    else:
        r = m
if nums[l] == target:
    ans = [l]
else:
    ans.append(-1)

