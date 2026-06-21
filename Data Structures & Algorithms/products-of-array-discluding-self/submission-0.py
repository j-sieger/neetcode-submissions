
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sums_list = []
        for i in range(len(nums)):
            if i ==0:
                sums_list.append(math.prod(nums[1:]))
            elif i == len(nums)-1:
                sums_list.append(math.prod(nums[:-1]))
            else:
                sums_list.append(math.prod(nums[:i])*math.prod(nums[i+1:]))

        return sums_list