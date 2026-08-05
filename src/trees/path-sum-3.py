from typing import Optional

from src.trees.support import TreeNode, build_tree


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        if not root:
            return 0

        result = []

        def dfs(node, ml):
            if not node:
                return

            ml = ml + [node.val]

            for item in range(len(ml) - 1, -1, -1):
                if sum(ml[item:]) == targetSum:
                    result.append(ml)

            dfs(node.left, ml)
            dfs(node.right, ml)

        dfs(root, [])

        return len(result)

root = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
print(Solution().pathSum(root, 22))


root = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
print(Solution().pathSum(root, 8))
