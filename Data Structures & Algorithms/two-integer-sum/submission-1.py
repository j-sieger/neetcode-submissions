class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        nums_map = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in nums_map:
                return [nums_map[remaining],i]
            nums_map[num] =i