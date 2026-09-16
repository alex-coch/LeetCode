from collections import deque
from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left_height = 0
        right_height = 0

        left = root
        right = root

        while left:
            left_height += 1
            left = left.left

        while right:
            right_height += 1
            right = right.right

        # Perfect binary tree
        if left_height == right_height:
            return (1 << left_height) - 1

        return (
            1
            + self.countNodes(root.left)
            + self.countNodes(root.right)
        )


root = build_tree([1,2,3,4,5,6, None])
print(Solution().countNodes(root))