class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack, ops = [], {'+', '-', '*', '/'}

        for token in tokens:

            if token not in ops:
                stack.append(token)
            else:
                b=int(stack.pop())
                a=int(stack.pop())

                if token == "+":
                    stack.append(str(a+b))
                if token == "-":
                    stack.append(str(a-b))
                if token == "*":
                    stack.append(str(a*b))
                if token == "/":
                    stack.append(str(int(a/b)))

        return int(stack[0])





        