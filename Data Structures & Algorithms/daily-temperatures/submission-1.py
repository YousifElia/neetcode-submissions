class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)
        return res

    # push 30,38,30,36,35,40,28
    # 28 will always be 0 no matter what
    #
    # for i in range(n)
    #   if temperature[i + 1] > temperature[i]: 
    #       result += 1
    # 
    # 
    # 