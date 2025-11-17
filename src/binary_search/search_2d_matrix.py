class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row, mid_col = divmod(mid, n)

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

        # mid, left, right, len_row = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if matrix[mid][0] < target:
        #         if matrix[mid][len_row] >= target:
        #             break
        #         left = left + 1
        #     else:
        #         if matrix[mid][len_row] <= target:
        #             break
        #         right = right - 1
        #
        # row = mid
        #
        # left, right = 0, len_row
        # while left <= right:
        #     mid = (left + right) // 2
        #     if matrix[row][mid] == target:
        #         return True
        #     elif matrix[row][mid] < target:
        #         left = left + 1
        #     else:
        #         right = right - 1
        # return False
