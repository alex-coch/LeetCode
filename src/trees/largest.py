from collections import deque
from typing import Optional, List

from src.trees.support import TreeNode, build_tree


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_max = float("-inf")

            for _ in range(len(queue)):
                node = queue.popleft()

                level_max = max(level_max, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level_max)

        return result

root = build_tree([3,None,30,10,None,None,15,None,45])
print(Solution().largestValues(root))

root = build_tree([1,3,2,5,3,None,9])
print(Solution().largestValues(root))