from collections import deque

from src.trees.support import print_bst


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        current = root

        while current:
            dummy = Node(0)
            tail = dummy

            # Проходим текущий уровень через next
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next

                if current.right:
                    tail.next = current.right
                    tail = tail.next

                current = current.next

            # Переходим на первый узел следующего уровня
            current = dummy.next

        return root

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = None
root.right.right = Node(7)

print_bst(Solution().connect(root))
