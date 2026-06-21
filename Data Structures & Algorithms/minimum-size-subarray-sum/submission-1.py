class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total , begin = 0,0    
        minArrayLen = float("inf")
           
        for end in range(len(nums)):
            total += nums[end]                                     
            while total>=target:                    
                minArrayLen = min(minArrayLen, end-begin+1)
                target = target + nums[begin] 
                begin = begin+1                 

        return 0 if minArrayLen == float("inf") else minArrayLen
