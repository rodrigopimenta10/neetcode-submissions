from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def bfs(x, y):
            q = deque([(x,y)])
            level = 0
            visited = set((x,y))
            while q:
                for _ in range(0,len(q)):
                    cur_x, cur_y = q.popleft()
                    #print(cur_x,cur_y)
                    if grid[cur_x][cur_y] == 0:
                        return level
                    for tup in directions:
                        new_x, new_y = cur_x+tup[0], cur_y+tup[1]
                        if 0 <= new_x <= len(grid)-1 \
                            and 0 <= new_y <= len(grid[0])-1 \
                            and grid[new_x][new_y] != -1:
                            if (new_x,new_y) not in visited:
                                #print(new_x,new_y)
                                q.append((new_x,new_y))
                                visited.add((new_x,new_y))
                level += 1

        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j)
