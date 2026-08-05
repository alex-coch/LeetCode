from collections import deque
from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    # dfs
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return (
                dfs(left.left, right.right)
                and
                dfs(left.right, right.left)
            )

        return dfs(root.left, root.right)

    # bfs
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #
    #     queue = deque([(root.left, root.right)])
    #
    #     while queue:
    #         left, right = queue.popleft()
    #
    #         if not left and not right:
    #             continue
    #
    #         if not left or not right:
    #             return False
    #
    #         if left.val != right.val:
    #             return False
    #
    #         queue.append((left.left, right.right))
    #         queue.append((left.right, right.left))
    #
    #     return True


root = build_tree([1,2,2,3,4,4,3])
print(Solution().isSymmetric(root))