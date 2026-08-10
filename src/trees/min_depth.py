from collections import deque
from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    # dfs better
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

    # dfs
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )




root = build_tree([2,None,3,None,4,None,5,None,6])
print(Solution().minDepth(root))

# root = build_tree([3,9,20,None,None,15,7])
# print(Solution().minDepth(root))