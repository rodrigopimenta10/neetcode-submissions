from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board),len(board[0])
        visited = set()
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i,j) not in visited:
                    # BFS
                    visited.add((i,j))

                    # If its on border:
                    if i == 0 or i == n-1 or j == 0 or j == m-1:
                        border_flag = True
                    else:
                        border_flag = False
                    cur_visited = set([(i,j)])
                    q = deque([(i,j)])
                    while q:
                        for _ in range(len(q)):
                            x, y = q.popleft()
                            for dx, dy in dirs:
                                new_x, new_y = x+dx, y+dy
                                if 0 <= new_x < n and 0 <= new_y < m \
                                    and board[new_x][new_y] == "O" \
                                    and (new_x,new_y) not in visited and (new_x,new_y) not in cur_visited:
                                    
                                    visited.add((new_x,new_y))
                                    cur_visited.add((new_x,new_y))
                                    q.append((new_x,new_y))
                                    if new_x == 0 or new_x == n-1 or new_y == 0 or new_y == m-1:
                                        border_flag = True

                    if border_flag == False:
                        for x, y in cur_visited:
                            board[x][y] = "X"
                    
                            
                            

        