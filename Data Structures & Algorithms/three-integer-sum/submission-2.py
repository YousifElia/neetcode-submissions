class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
               break

            if i > 0 and a == nums[i - 1]:
                continue

            i,j,k = 0, i+1, len(nums) - 1
            while j < k:
                threeSum = a + nums[j] + nums[k]
                if threeSum < 0:
                    j += 1
                elif threeSum > 0: 
                    k -= 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res
# j == left pointer, k == right pointer

# j = i+1
#
# -4, -1, -1, 0, 1, 2
#  i,  j,   ,  ,  , k
#  i + j + k = -3 (increment i++)
#
# -4, -1, -1, 0, 1, 2
#   ,  i,  j,  ,  , k
#  i + j + k = 0 (save result + increment)
#
# -4, -1, -1, 0, 1, 2
#   ,   ,  i, j,  , k
#  i + j + k = 1 (decrement k--)
#
# -4, -1, -1, 0, 1, 2
#   ,   ,   , i, j, k
#  i + j + k = 0 (save result + stop)