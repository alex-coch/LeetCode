from src.trees.support import TreeNode, build_tree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ml = []

        def dfs(node, mv):
            if not node:
                return None

            if node.val >= mv:
                mv = node.val
                ml.append(node.val)

            dfs(node.left, mv)
            dfs(node.right, mv)

        dfs(root, root.val)
        return len(ml)


root = build_tree([3,3,None,4,2])
print(Solution().goodNodes(root))

root = build_tree([3,1,4,3,None,1,5])
print(Solution().goodNodes(root))