class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        stack = []
        res = 0

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                
                if token == "+":
                    res = left + right
                elif token == "-":
                    res = left - right
                elif token == "*":
                    res = left * right
                else:
                    res = int(left / right)
                stack.append(res)
        return stack[-1]

# 1, 2, +, 3, *, 4, -  (- is at the top)
# 
# []
# [1]
# [1, 2]
# [1, 2] (sees + adds them together)
# [3]
# [3, 3]
# [3, 3] (sees * multiplies them tg)
# [9, 4] 
# [9, 4] (sees - subtracts them tg)
# [5] 