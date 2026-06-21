class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res =[]
        n = len(nums2)
        for num1 in nums1:
            nextGreater = -1
            for i in range(n - 1, -1, -1):
                if nums2[i]> num1:
                    nextGreater = nums2[i]
                elif nums2[i] == num1:   
                    break           
            res.append(nextGreater)
        return res

        # stack = []
        # hash_map = {}
        # for num in nums2:
        #     while stack and num > stack[-1]:
        #         hash_map[stack.pop()]=num
        #     stack.append(num)

        # while stack:
        #     hash_map[stack.pop()]=-1        

        # res = []
        # for num in nums1:
        #     res.append(hash_map[num])
        # return res
    


        