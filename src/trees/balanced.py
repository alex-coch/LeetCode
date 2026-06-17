from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: TreeNode) -> int:
            if not node:
                return 0

            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced

            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced

            # Check balance condition for current node
            if abs(left_height - right_height) > 1:
                return -1

            # Return actual height of current node
            return max(left_height, right_height) + 1

        return check_height(root) != -1


# root = build_tree([1,2,2,3,None,None,3,4,None,None,4])
# print(Solution().isBalanced(root))
#
# root = build_tree([1,2,2,3,3,None,None,4,4])
# print(Solution().isBalanced(root))

# root = build_tree([3,9,20,None,None,15,7])
# print(Solution().isBalanced(root))

# root = build_tree([1])
# print(Solution().isBalanced(root))

root = build_tree([1,None,2,None,3])
print(Solution().isBalanced(root))