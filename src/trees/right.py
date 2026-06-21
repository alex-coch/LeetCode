from typing import Optional, List

from src.trees.support import TreeNode, build_tree


from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        # if not root:
        #     return []
        #
        # result = []
        # queue = deque([root])
        #
        # while queue:
        #     level_size = len(queue)
        #
        #     for i in range(level_size):
        #         node = queue.popleft()
        #
        #         if node.left:
        #             queue.append(node.left)
        #
        #         if node.right:
        #             queue.append(node.right)
        #
        #         # Last node in the level
        #         if i == level_size - 1:
        #             result.append(node.val)
        #
        # return result

        # DFS
        result = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result


root = build_tree([1,2,3,None,5,None,4])
print(Solution().rightSideView(root))