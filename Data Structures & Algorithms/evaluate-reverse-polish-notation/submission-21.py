class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                first = stack.pop()
                stack.append(stack.pop() - first)
            elif token == "/":
                second = stack.pop()
                stack.append(int(stack.pop() / second))
            else:
                stack.append(int(token))

        return stack.pop()
