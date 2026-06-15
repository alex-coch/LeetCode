from typing import Optional

from src.trees.support import TreeNode, prepare_bst, build_tree


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return diameter

root = build_tree([1,2,3,4,5, None, None])
print(Solution().diameterOfBinaryTree(root))

root = build_tree([1, 2, None, None, None])
print(Solution().diameterOfBinaryTree(root))