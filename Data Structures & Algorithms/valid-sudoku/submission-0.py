class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def row_valid(board):
            for row in range(0,len(board)):
                s = set()
                for col in range(0,len(board[0])):
                    if board[row][col] != '.' and board[row][col] in s:
                        return False
                    else:
                        s.add(board[row][col])
            return True

        def col_valid(board):
            for col in range(0,len(board[0])):
                s = set()
                for row in range(0,len(board)):
                    if board[row][col] != '.' and board[row][col] in s:
                        return False
                    else:
                        s.add(board[row][col])
            return True

        def submatrix_valid(board):
            k, j = 0, 0
            s = set()
            while k != 9:
                while j != 9:
                    for row in range(k,k+3):
                        for col in range(j,j+3):
                            if board[row][col] != '.' and board[row][col] in s:
                                return False
                            else:
                                s.add(board[row][col])
                            #print(f"({row},{col}):{board[row][col]}", end=",")
                    s = set()
                    j += 3
                #print()
                k += 3
                j = 0

            return True


        return row_valid(board) and col_valid(board) and submatrix_valid(board)


"""
board=[
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]

"""
