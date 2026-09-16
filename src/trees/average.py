from collections import deque
from typing import Optional, List

from src.trees.support import TreeNode, build_tree


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []

        if not root:
            return result

        q = deque([root])
        cnt = 0

        while q:
            ml = []
            for _ in range(len(q)):
                item = q.popleft()
                if item:
                    ml.append(item.val)
                    q.append(item.left)
                    q.append(item.right)
            if ml:
                result.append(sum(ml)/len(ml))
            cnt += 1

        return result


root = build_tree([3,None,30,10,None,None,15,None,45])
print(Solution().averageOfLevels(root))

root = build_tree([3,9,20,15,7, None, None])
print(Solution().averageOfLevels(root))