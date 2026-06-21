class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}  # remainder -> end index
        total = 0
        for i, num in enumerate (nums):
            total += num
            r = total % k
            if r not in remainder:
                remainder[r]=i
            elif i-remainder[r]>=2: # sub array length
                return True

        return False

        