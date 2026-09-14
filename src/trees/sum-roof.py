from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ml = []

        def dfs(node, tree):
            if not node:
                return ""

            value = str(tree) + str(node.val)
            if not node.left and not node.right:
                ml.append(value)

            dfs(node.left, value)
            dfs(node.right, value)

        dfs(root, 0)

        return sum(map(int,ml))

root = build_tree([9])
print(Solution().sumNumbers(root))

root = build_tree([4,9,0,5,1])
print(Solution().sumNumbers(root))

root = build_tree([1,2,3])
print(Solution().sumNumbers(root))