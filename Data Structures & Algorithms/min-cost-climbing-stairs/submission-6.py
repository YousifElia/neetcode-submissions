class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) # top of the stair case is cost of 0
        one, two = 0, 1
        
        for current in range(2, len(cost)):
            if cost[one] < cost[two]:
                cost[current] += cost[one]
            else:
                cost[current] += cost[two]
                
            one += 1
            two += 1
        return cost[-1]
