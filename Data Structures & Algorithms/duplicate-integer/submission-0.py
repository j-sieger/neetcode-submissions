class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)        
        n = len(nums_sorted)
        for i in range(1,n):
            if nums_sorted[i] == nums_sorted[i-1]:
                return True
        return False
            

