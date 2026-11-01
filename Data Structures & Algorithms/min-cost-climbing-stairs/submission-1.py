class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two, temp = 0, 1, 0
        if len(cost) == 3:
            temp += cost[two]
            
        while two < len(cost):
            if cost[one] < cost[two]:
                temp += cost[one]

                one += two
                two += 1
            else:
                temp += cost[two]
                one = two + 1
                two = one + 1
        return temp