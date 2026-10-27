from collections import Counter
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Edge case: no cooldown means just run tasks one after another.
        if n == 0:
            return len(tasks)
        
        # Count frequencies and build a max-heap (using negatives)
        task_counts = Counter(tasks)
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)
        
        # Queue for tasks in cooldown: (ready_time, count)
        cooldown = deque()
        time = 0
        
        while max_heap or cooldown:
            time += 1
            
            # If a task is available, schedule it.
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)  # since counts are negative
                if cnt < 0:  # if there are still executions left for this task
                    # Append task to cooldown with the time it will be ready
                    cooldown.append((time + n, cnt))
            
            # If the task at the front of cooldown is ready, push it back into the heap.
            if cooldown and cooldown[0][0] == time:
                ready_time, cnt = cooldown.popleft()
                heapq.heappush(max_heap, cnt)
        
        return time