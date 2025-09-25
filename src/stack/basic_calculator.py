class Solution:
    def calculate(self, s: str) -> int:
        # not so elegant but works
        def inner_stack(stack: list) -> int:
            if stack[-1] == ")":
                stack.pop()
                stack.append(inner_stack(stack))
            in_result = 0
            while stack and stack[-1] != "(":
                if stack[-1] == ")":
                    stack.pop()
                    stack.append(inner_stack(stack))
                in_element = int(stack.pop())
                in_result = in_result + in_element if stack[-1]=="(" or stack[-1] == "+" else in_result - in_element
                if stack:
                    if stack.pop() == "(":
                        return in_result
            if stack and stack[-1] == "(":
                stack.pop()
            return in_result

        stack = []
        for char in s:
            if char == " ":
                continue
            if char.isdigit() and stack and stack[-1][-1].isdigit():
                stack.append(stack.pop() + char)
            else:
                stack.append(char)

        result = 0
        while stack:
            element = stack.pop()
            if element == ")":
                element = inner_stack(stack)
            else:
                element = int(element)
            result = result + element if not stack or stack[-1] == "+" else result - element
            if stack:
                stack.pop()

        return result
