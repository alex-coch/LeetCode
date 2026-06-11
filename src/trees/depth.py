from typing import Optional

from src.trees.support import TreeNode, prepare_bst, build_tree, print_bst


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _maxDepth(node, level):
            if not node:
                return level

            level += 1
            ll1 = _maxDepth(node.left, level)
            ll2 = _maxDepth(node.right, level)

            return max(ll1, ll2)

        if not root:
            return 0

        result = 1
        l1 = _maxDepth(root.left, result)
        l2 = _maxDepth(root.right, result)

        return max(l1, l2)


node = build_tree([3,9,20,None,None,15,7])
print(Solution().maxDepth(node))