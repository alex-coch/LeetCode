from typing import List


class Solution:
    # DFS + Backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def dfs(open_count, close_count):
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # Add "("
            if open_count < n:
                current.append("(")  # Choose
                dfs(open_count + 1, close_count)  # Explore
                current.pop()  # Unchoose

            # Add ")"
            if close_count < open_count:
                current.append(")")  # Choose
                dfs(open_count, close_count + 1)  # Explore
                current.pop()  # Unchoose

        dfs(0, 0)

        return result

print(Solution().generateParenthesis(3))