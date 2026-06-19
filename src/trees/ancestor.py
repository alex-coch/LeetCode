from src.trees.support import TreeNode, build_tree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            else:
                return curr

root = build_tree([6,2,8,0,4,7,9,None,None,3,5])
p = TreeNode(2)
q = TreeNode(8)
print(Solution().lowestCommonAncestor(root, p, q).val)

root = build_tree([6,2,8,0,4,7,9,None,None,3,5])
p = TreeNode(2)
q = TreeNode(4)
print(Solution().lowestCommonAncestor(root, p, q).val)

root = build_tree([6,2,8,0,4,7,9,None,None,3,5])
p = TreeNode(3)
q = TreeNode(5)
print(Solution().lowestCommonAncestor(root, p, q).val)




