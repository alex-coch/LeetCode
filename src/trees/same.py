from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and not q or not p and q:
            return False

        if p and q and p.val != q.val:
            return False

        # if p.left and not q.left or not p.left and q.left:
        #     return False

        if not self.isSameTree(p.left, q.left):
            return False

        # if p.right and not q.right or not p.right and q.right:
        #     return False

        if not self.isSameTree(p.right, q.right):
            return False

        return True


p = build_tree([])
q = build_tree([0])
print(Solution().isSameTree(p, q))

p = build_tree([1,2,3])
q = build_tree([1,2,3])
print(Solution().isSameTree(p, q))

p = build_tree([1,2])
q = build_tree([1, None, 2])
print(Solution().isSameTree(p, q))

p = build_tree([1,2,1])
q = build_tree([1,1,2])
print(Solution().isSameTree(p, q))