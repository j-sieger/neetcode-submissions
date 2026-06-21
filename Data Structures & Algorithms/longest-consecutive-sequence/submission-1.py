class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # sorting and unique values
        sorted_nums = sorted(set(nums))
        longest_streak = 1
        current_streak = 1        
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i]-1 == sorted_nums[i-1]:
                current_streak =current_streak + 1
                if current_streak > longest_streak:
                    longest_streak = current_streak
            else:
                current_streak = 1
        return longest_streak
        