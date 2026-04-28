class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for sym in tokens:
            if sym == "+":
                stack.append(stack.pop() + stack.pop())
            elif sym == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif sym == "*":
                stack.append(stack.pop() * stack.pop())
            elif sym == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(sym))
        return stack[0]