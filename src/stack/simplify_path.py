class Solution:
    def simplifyPath(self, path: str) -> str:
        def process_folder(folder, stack):
            if folder == ".." and stack:
                stack.pop()
            elif folder != "." and folder != "..":
                stack.append((folder))
        stack = []
        stack.append("")
        folder = ""
        for char in path[1:]:
            if char != "/":
                folder += char
            elif folder:
                process_folder(folder, stack)
                folder = ""
        if folder:
            process_folder(folder, stack)
        if stack and stack[-1] == "/":
            stack.pop()
        result = "/".join(stack) if stack else "/"
        return result if result.startswith("/") else f"/{result}"
