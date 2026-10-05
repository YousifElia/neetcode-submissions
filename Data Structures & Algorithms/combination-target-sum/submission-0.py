class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i, cur, total): 
            if total == target: # base cases
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i]) # append the nums[i] onto the list
            dfs(i, cur, total + nums[i]) # recall the function (recursive)
            cur.pop() # pop the current bc of line 12 (clean up the current)
            dfs(i + 1, cur, total) # we move to the next nums #
        
        dfs(0, [], 0) # we start at index 0, empty array, and total starts at 0
        return res