from collections import deque
from typing import Optional, List

from src.trees.support import TreeNode, build_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

root = build_tree([3,9,20,None,None,15,7])
print(Solution().levelOrder(root))