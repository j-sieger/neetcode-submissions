class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
    # O(n^2) Solution
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a>0: # all the numbers are postives so 3 sums cant be zero
                break            
            l = i+1
            r = len(nums)-1
            while l<r:
                if  a + nums[l] + nums[r] >0:
                    r -=1
                elif  a + nums[l] + nums[r]<0:
                    l +=1

                else: # when sum is 0                    
                    res.append([ a, nums[l] , nums[r]])
                    l +=1
                    r -=1
                    while l<r: # to check new num[l] is not same as prev nums[l]
                        # This avoid duplicates. even though we have a value muliple times we want to consider it only once
                        if nums[l] == nums[l-1]:                            
                            l +=1
                        break



    # My solution o(n3)    
        prevMap = {}
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        triplet = sorted([nums[i],nums[j],nums[k]])
                        if triplet not in res:
                            res.append(triplet)                    
        return res