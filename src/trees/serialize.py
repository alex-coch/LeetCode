from collections import deque

from src.trees.support import build_tree, print_bst, TreeNode

# bfs

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        values = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                values.append(None)
                continue

            values.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        while values and values[-1] is None:
            values.pop()

        return values

    def deserialize(self, data):
        """Decodes encoded data to a tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = data

        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue and index < len(values):
            node = queue.popleft()

            # Restore the left child.
            if index < len(values) and values[index] is not None:
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)

            index += 1

            # Restore the right child.
            if index < len(values) and values[index] is not None:
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)

            index += 1

        return root

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()

ml = [1,2,3,None,None,4,5]
root = build_tree(ml)

print(ser.serialize(root))
print_bst(deser.deserialize(ml))
# ans = deser.deserialize(ser.serialize(root))


# dfs

class Codec:

    def serialize(self, root):
        values = []

        def dfs(node):
            if not node:
                values.append(None)
                return

            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return values

    def deserialize(self, data):
        values = iter(data)

        def dfs():
            value = next(values)

            if value is None:
                return None

            node = TreeNode(value)
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


ser = Codec()
deser = Codec()

ml = [1, 2, 3, None, None, 4, 5]
root = build_tree(ml)

serialized = ser.serialize(root)

print(serialized)
print_bst(deser.deserialize(serialized))