from collections import defaultdict
from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
            0.      2      3
             \.      \.     \
              1.       0.     0     
        """
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)

        for x, y in edges:
            #print(f'{x},{y},{graph}')
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        def dfs(x, parent):
            visited.add(x)
            if graph[x]:
                for child in graph[x]:
                    if child not in visited:
                        if dfs(child, x):
                            return True
                    elif child != parent:
                        return True
            return False
        
        for x in graph:
            if x not in visited:
                if dfs(x, None):
                    return False
        print(visited)
        return True


        # Look for cycle
        # visisted = set()
        # q = deque([x])
        # while q:
        #     print(q)
        #     for _ in range(0,len(q)):
        #         cur = q.popleft()
        #         if cur in graph and cur not in visited:
        #             for y in graph[cur]:
        #                 q.append(y)
        #                 visited.add(y)
        return True

        
            
