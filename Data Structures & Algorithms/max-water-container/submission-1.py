class Solution:
    def maxArea(self, heights: List[int]) -> int:
        MaxArea =0
        l = 0
        r = len(heights)-1
        while l<r:
            area = min(heights[l],heights[r]) * (r-l)
            if area > MaxArea:
                MaxArea = area
            if heights[l]> heights[r]:
                r -=1
            elif heights[r]>= heights[l]:
                l +=1
            
        return MaxArea
        
    # o(n^2) solution
        # MaxArea = 0
        # for i, num in enumerate(heights):
        #     for j in range(i+1, len(heights)):
        #         area = (j-i) * min(heights[i],heights[j])
        #         if area > MaxArea:
        #             MaxArea = area
        # return MaxArea


        