from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0

        if not root:
            return result

        def dfs(node):
            nonlocal result

            if not node:
                return 0

            if low <= node.val <= high:
                result += node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

root = build_tree([10,5,15,3,7,None,18])
print(Solution().rangeSumBST(root=root, low = 7, high = 15))

root = build_tree([10,5,15,3,7,13,18,1,None,6])
print(Solution().rangeSumBST(root=root, low = 6, high = 10))
