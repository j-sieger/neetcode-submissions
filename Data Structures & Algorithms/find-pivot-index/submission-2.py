class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = totalSum-leftSum-nums[i]
            if leftSum == rightSum:
                return i
            leftSum = leftSum+nums[i]
        return -1
    # def pivotIndex(self, nums: List[int]) -> int:
    #     prefixSum_left = [0]
    #     prefixSum_right = [0]
    #     left_sum = 0
    #     right_sum = 0 
    #     n = len(nums)
    #     for i in range(n):
    #         left_sum = left_sum+nums[i]
    #         right_sum = right_sum + nums[n-i-1]
    #         prefixSum_left.append(left_sum)
    #         prefixSum_right.append(right_sum)                
    #     print(prefixSum_left)
    #     print(prefixSum_right)
    #     for i in range(n):
    #         if prefixSum_left[i] == prefixSum_right[n-i-1]:
    #             return i
    #     return -1  
            




    # def pivotIndex(self, nums: List[int]) -> int:
    #     for i in range(len(nums)):
    #         print(i)
    #         if sum(nums[:i]) == sum(nums[i+1:]):
    #             return i
    #     return -1