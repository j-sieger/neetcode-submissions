class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }
        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
            # print(res,curSum, prefixSums)
        return res
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     curr_sum = 0
    #     no_of_subArrays =0
    #     left = 0
    #     for i in range(len(nums)):
    #         curr_sum = curr_sum+nums[i]
    #         if curr_sum == k:
    #             no_of_subArrays +=1
    #             print("if:",left,i)
    #         while curr_sum >k:
    #             curr_sum -= nums[left]
    #             left +=1
    #             if curr_sum == k:
    #                 no_of_subArrays +=1
    #                 print("wl:",left,i)
    #             # left +=1
    #     return no_of_subArrays


        