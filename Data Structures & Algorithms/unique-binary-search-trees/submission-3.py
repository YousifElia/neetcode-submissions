from functools import cache

class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dp(k: int) -> int:
            if k <= 1:
                return 1
            res = 0
            for i in range(1, k + 1):
                left = dp(i - 1)
                right = dp(k - i)
                res += left * right
            return res

        return dp(n)
