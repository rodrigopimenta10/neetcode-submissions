class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])



        l, r = 0, m * n - 1
        while l <= r:
            mid = (r - l) // 2 + l
            row = mid // n
            col = mid % n
            print(l, r, row, col)
            mid_val = matrix[row][col]
            #print(mid_val, l, r)

            if target == mid_val:
                return True
            elif target > mid_val:
                l = mid + 1
            else:
                #target < mid_val
                r = mid - 1
        return False