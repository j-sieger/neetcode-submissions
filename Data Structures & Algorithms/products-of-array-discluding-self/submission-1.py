
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:        
#     # My solutions
#         sums_list = []
#         for i in range(len(nums)):
#             if i ==0:
#                 sums_list.append(math.prod(nums[1:]))
#             elif i == len(nums)-1:
#                 sums_list.append(math.prod(nums[:-1]))
#             else:
#                 sums_list.append(math.prod(nums[:i])*math.prod(nums[i+1:]))

#         return sums_list
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #         How it works:
# 1. Left Pass: Travel from left to right. Store the running product of all elements before the current index.
# 2. Right Pass: Travel from right to left. Multiply the existing values by the running product of all elements after the current index.

        length = len(nums)
        res = [1] * length
        
        # Step 1: Calculate Prefix products
        # res[i] contains the product of all elements to the left of i
        prefix = 1
        for i in range(length):
            res[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate Suffix products on the fly
        # Multiply the existing prefix product by the suffix product
        suffix = 1
        for i in range(length - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res