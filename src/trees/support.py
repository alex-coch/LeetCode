from collections import deque


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


def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# node = prepare_bst([4,2,7,1,3,6,9])
# print_bst(node)
