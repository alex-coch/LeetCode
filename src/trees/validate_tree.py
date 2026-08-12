from collections import deque
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n

        # 1. У каждого узла может быть только один родитель
        for node in range(n):
            for child in (leftChild[node], rightChild[node]):
                if child == -1:
                    continue

                if parent[child] != -1:
                    return False

                parent[child] = node

        # 2. Должен быть ровно один root
        roots = []

        for node in range(n):
            if parent[node] == -1:
                roots.append(node)

        if len(roots) != 1:
            return False

        root = roots[0]

        # 3. Обходим дерево и проверяем, что посетили все узлы
        visited = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node in visited:
                return False

            visited.add(node)

            if leftChild[node] != -1:
                queue.append(leftChild[node])

            if rightChild[node] != -1:
                queue.append(rightChild[node])

        return len(visited) == n

print(Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]))