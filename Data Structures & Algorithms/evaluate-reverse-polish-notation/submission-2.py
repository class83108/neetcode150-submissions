class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            print(stack)
            if token not in operators:
                stack.append(int(token))
            
            else:
                if token == "+":
                   stack.append(stack.pop() + stack.pop())

                elif token == "-":
                    first, second = stack.pop(), stack.pop()
                    stack.append(second - first)
                
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                
                elif token == "/":
                    first, second = stack.pop(), stack.pop()
                    stack.append(int(float(second) / first))
        
        return stack[0]
        