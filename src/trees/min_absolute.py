from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float("inf")

        def inorder(node):
            nonlocal prev, min_diff

            if not node:
                return

            inorder(node.left)

            if prev is not None:
                min_diff = min(
                    min_diff,
                    node.val - prev
                )

            prev = node.val

            inorder(node.right)

        inorder(root)

        return min_diff

root = build_tree([4, 2, 6, 1, 3, None, None])

print(Solution().getMinimumDifference(root))