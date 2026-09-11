class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(column):
                if matrix[i][j] == target:
                    return True
        return False
        

# O(n * m) time and O(1) space complexity (not optimial)
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