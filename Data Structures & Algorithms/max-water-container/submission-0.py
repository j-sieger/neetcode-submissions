class Solution:
    def maxArea(self, heights: List[int]) -> int:
        MaxArea = 0
        for i, num in enumerate(heights):
            for j in range(i+1, len(heights)):
                area = (j-i) * min(heights[i],heights[j])
                if area > MaxArea:
                    MaxArea = area
        return MaxArea


        