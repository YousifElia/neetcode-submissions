class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        newrob1, newrob2 = 0,0

        if len(nums) == 1:
            return nums[0]

        for i in nums[:-1]:
            temp = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = temp
        for j in nums[1:]:
            temp2 = max(newrob1 + j, newrob2)
            newrob1 = newrob2
            newrob2 = temp2
        return max(newrob2, rob2)