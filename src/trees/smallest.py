from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = 0

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)

            self.count += 1
            if self.count == k:
                self.answer = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.answer


root = build_tree([3,1,4,None,2])
print(Solution().kthSmallest(root, 1))

root = build_tree([5,3,6,2,4,None,None,1])
print(Solution().kthSmallest(root, 3))