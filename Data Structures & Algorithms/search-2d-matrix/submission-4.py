class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        row, column = len(matrix), len(matrix[0])
        l, r = 0, column - 1
        
        while l <= r:
            m = l + (r - 1) // 2
            ROWS, COLUMNS = m // column, m % column
            if target > matrix[ROWS][COLUMNS]:
                l = m + 1
            elif target < matrix[ROWS][COLUMNS]:
                r = m - 1
            else:
                return True
        return False


# Sorted 2D Array
# Find the Middle 
# low, high = 0, len(arr) - 1
#  len(List[List[int]]) / 2
#
#  if List[List[int]] > target:
#       List[List[int]] / 4
#  elif List[List[int]] < target:
#       List[List[int]] * 2
#  else return