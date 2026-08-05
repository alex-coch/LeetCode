from typing import Optional, List

from src.trees.support import TreeNode, build_tree


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        if not root:
            return []

        def dfs(node, ml):
            if not node:
                return 0

            ml = ml + [node.val]

            if not node.left and not node.right and sum(ml) == targetSum:
                result.append(ml)

            dfs(node.left, ml)
            dfs(node.right, ml)

        dfs(root, [])

        return result

root = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
print(Solution().pathSum(root, 22))

root = build_tree([1,2,3])
print(Solution().pathSum(root, 5))