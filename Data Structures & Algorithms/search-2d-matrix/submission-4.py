class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # In accending order
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1

        while l <= r:
            mid = (l + r) // 2
            # get the row and the col
            row = mid // n
            col = mid % n
            val = matrix[row][col]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
        return False