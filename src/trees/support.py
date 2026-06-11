class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root: TreeNode | None, val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def prepare_bst(values: list[int]) -> TreeNode | None:
    root = None

    for val in values:
        root = insert(root, val)

    return root


def print_bst(root):
    if not root:
        return None

    print(root.val, end=" ")
    print_bst(root.left)
    print_bst(root.right)


# node = prepare_bst([4,2,7,1,3,6,9])
# print_bst(node)
