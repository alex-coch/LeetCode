class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = result_str = ""
        stack = []
        for char in s:
            if char == '(':
                stack.append((char, len(result)))
                result += char
            if char == ')':
                if len(stack) > 0:
                    stack.pop()
                    result += char
            if char not in '()':
                result += char
        idxs = {item[1] for item in stack}
        for idx, item in enumerate(result):
            if idx not in idxs:
                result_str += item
        return result_str

