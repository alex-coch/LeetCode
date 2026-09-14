from typing import Optional

from src.trees.support import TreeNode, build_tree


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = 0
        self.ml = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            self.ml.append(node.val)
            dfs(node.right)

        dfs(root)

        self.lenght = len(self.ml)

    def next(self) -> int:
        val = self.ml[self.cur]
        self.cur += 1
        return val

    def hasNext(self) -> bool:
        return self.cur < self.lenght

root = build_tree([7, 3, 15, None, None, 9, 20])

# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
