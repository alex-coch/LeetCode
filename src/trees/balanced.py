from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node):
            if not node:
                return 0

            left = get_depth(node.left)
            right = get_depth(node.right)

            return 1 + max(left, right)

        if not root or (not root.left and not root.right):
            return True

        depth_left = get_depth(root.left)
        depth_right = get_depth(root.right)
        if abs(depth_left - depth_right) <= 1:
            return True

        return False


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