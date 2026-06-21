class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_map = {}
        for num in nums2:
            while stack and num > stack[-1]:
                hash_map[stack.pop()]=num
            stack.append(num)

        while stack:
            hash_map[stack.pop()]=-1        

        res = []
        for num in nums1:
            res.append(hash_map[num])
        return res
    

        