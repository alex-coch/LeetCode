from typing import Optional

from src.trees.support import TreeNode, build_tree, print_bst


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root

        while current:
            if current.left:
                predecessor = current.left

                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = current.right
                current.right = current.left
                current.left = None

            current = current.right
        print_bst(root)


root = build_tree([1,2,5,3,4,None,6])
Solution().flatten(root)