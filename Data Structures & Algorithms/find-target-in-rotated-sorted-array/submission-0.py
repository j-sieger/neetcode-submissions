# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
        
#         res = -1
#         l , r = 0, len(nums)-1
#         while l<=r:
#             if nums[l]==target:
#                 res = l
#                 print("final l:", l)
#                 break
#             elif nums[r] == target:
#                 res = r
#                 break
#             m = (r+l)//2
#             # res = min(res,nums[m])
#             print(res," m: ", m)
#             if nums[m]>=nums[l]:
#                 l = m+1
#             else:
#                 r = m-1
#             print("l.r::",l,r)
#         print("final:",res)
#         return res
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)