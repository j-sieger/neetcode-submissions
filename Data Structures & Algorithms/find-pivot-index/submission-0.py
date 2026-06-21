class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            print(i)
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1