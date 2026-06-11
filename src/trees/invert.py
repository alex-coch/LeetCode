# Definition for a binary tree node.
from typing import Optional

from src.trees.support import prepare_bst, print_bst


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



node = prepare_bst([4,2,7,1,3,6,9])

node_new = Solution().invertTree(root=node)
print_bst(node_new)