from collections import deque
from typing import List


class Solution:
    # dfs
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row: int, col: int) -> None:
            if (
                    row < 0
                    or row >= rows
                    or col < 0
                    or col >= cols
                    or grid[row][col] != "1"
            ):
                return

            grid[row][col] = "0"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands

    # bfs
    # def numIslands(self, grid: list[list[str]]) -> int:
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     islands = 0
    #
    #     directions = [
    #         (-1, 0),
    #         (1, 0),
    #         (0, -1),
    #         (0, 1),
    #     ]
    #
    #     for row in range(rows):
    #         for col in range(cols):
    #             if grid[row][col] != "1":
    #                 continue
    #
    #             islands += 1
    #             grid[row][col] = "0"
    #
    #             queue = deque([(row, col)])
    #
    #             while queue:
    #                 current_row, current_col = queue.popleft()
    #
    #                 for row_offset, col_offset in directions:
    #                     next_row = current_row + row_offset
    #                     next_col = current_col + col_offset
    #
    #                     if (
    #                         0 <= next_row < rows
    #                         and 0 <= next_col < cols
    #                         and grid[next_row][next_col] == "1"
    #                     ):
    #                         grid[next_row][next_col] = "0"
    #                         queue.append((next_row, next_col))
    #
    #     return islands



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))
