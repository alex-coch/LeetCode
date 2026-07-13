from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(
            node: Optional[TreeNode],
            lower: float,
            upper: float
        ) -> bool:
            if not node:
                return True

            if not lower < node.val < upper:
                return False

            return (
                validate(node.left, lower, node.val)
                and validate(node.right, node.val, upper)
            )

        return validate(root, float("-inf"), float("inf"))

root = build_tree([5,4,6,None,None,3,7])
print(Solution().isValidBST(root))

root = build_tree([0,-1])
print(Solution().isValidBST(root))

root = build_tree([1,1])
print(Solution().isValidBST(root))

root = build_tree([2,1,3])
print(Solution().isValidBST(root))

root = build_tree([5,1,4,None,None,3,6])
print(Solution().isValidBST(root))