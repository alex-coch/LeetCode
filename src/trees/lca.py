from src.trees.support import TreeNode, build_tree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right


def find_node(root, val):
    if not root:
        return None

    if root.val == val:
        return root

    return find_node(root.left, val) or find_node(root.right, val)

root = build_tree([3,5,1,6,2,0,8,None,None,7,4])

p = find_node(root, 5)
q = find_node(root, 1)

lca = Solution().lowestCommonAncestor(root, p, q)

print(lca.val)
