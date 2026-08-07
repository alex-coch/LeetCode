from typing import Optional, List

from src.trees.support import TreeNode, print_bst, build_tree


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result



root = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])
print(Solution().inorderTraversal(root))

root = build_tree([1,None,2,3])
print(Solution().inorderTraversal(root))