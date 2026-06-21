class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #no.of rows
        n = len(matrix[0]) # no.of cols
        left = 0
        right= (m*n)-1
        while left<=right:
            mid = (left+right)//2
            row_idx = mid//n
            column_idx = mid%n
            # print(row_idx,column_idx)
            if matrix[row_idx][column_idx] == target:
                return True
            elif matrix[row_idx][column_idx] < target:
                left = mid+1
            else:
                right = mid-1
        return False
        