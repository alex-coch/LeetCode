from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # leaf
        if not root.left and not root.right:
            return targetSum == root.val

        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining)
            or
            self.hasPathSum(root.right, remaining)
        )


root = build_tree([1, 2])
targetSum = 1
print(Solution().hasPathSum(root, targetSum))

root = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
targetSum = 22
print(Solution().hasPathSum(root, targetSum))