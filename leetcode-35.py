class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=-1,len(nums)
        while l+1!=r:
            m = l+r>>1
            if nums[m] <= target:l = m
            else:r = m
        return l if nums[l] == target else r
        
