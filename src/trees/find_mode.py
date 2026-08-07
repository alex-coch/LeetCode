from collections import Counter
from typing import Optional, List

from src.trees.support import TreeNode, build_tree


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hm = {}
        result = []

        if not root:
            return result

        def dfs(node):
            if not node:
                return

            hm[node.val] = hm.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        sml = sorted(hm.items(), key=lambda x: x[1], reverse=True)
        mf = 0
        for key, value in sml:
            if value < mf:
                break
            result.append(key)
            mf = value

        return result


root = build_tree([1,None,2,2,2])
print(Solution().findMode(root))

root = build_tree([0])
print(Solution().findMode(root))
