from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and not subRoot or not root and subRoot:
            return False

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and not q or not p and q:
            return False

        if p and q and p.val != q.val:
            return False

        if not self.isSameTree(p.left, q.left):
            return False

        if not self.isSameTree(p.right, q.right):
            return False

        return True

root = build_tree([3,4,5,1,2])
subRoot = build_tree([4,1,2])

print(Solution().isSubtree(root, subRoot))
