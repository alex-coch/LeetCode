from typing import List, Optional

from src.trees.support import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {
            value: i
            for i, value in enumerate(inorder)
        }

        post_index = len(postorder) - 1

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal post_index

            if left > right:
                return None

            root_value = postorder[post_index]
            post_index -= 1

            root = TreeNode(root_value)

            mid = inorder_index[root_value]

            # Важно: сначала строим RIGHT,
            # потому что postorder читаем с конца
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)


