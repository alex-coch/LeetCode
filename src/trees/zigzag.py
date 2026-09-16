from collections import deque

from src.trees.support import TreeNode, build_tree


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []

        if not root:
            return result

        q = deque([root])
        cnt = 1

        while q:
            ml = []
            for _ in range(len(q)):
                item = q.popleft()
                if item:
                    ml.append(item.val)
                    q.append(item.left)
                    q.append(item.right)
            if ml:
                result.append(ml if cnt%2 else ml[-1::-1])
            cnt += 1

        return result


root = build_tree([3,9,20,None,None,15,7])
print(Solution().zigzagLevelOrder(root))