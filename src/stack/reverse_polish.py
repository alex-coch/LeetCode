class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                match token:
                    case '+':
                        stack.append(first + second)
                    case '-':
                        stack.append(first - second)
                    case '*':
                        stack.append(first * second)
                    case '/':
                        stack.append(int(first / second))
        return stack.pop()

# print(Solution().evalRPN(["2","1","+","3","*"]))
# print(Solution().evalRPN(["4","13","5","/","+"]))
# print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))