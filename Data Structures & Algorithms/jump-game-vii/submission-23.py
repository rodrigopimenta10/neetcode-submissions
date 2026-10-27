from collections import deque
class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = deque([0])
        farthest = 0

        while q:
            cur = q.popleft()
            for i in range(max(cur + minJump,farthest+1), min(cur + maxJump+1,n)):
                if s[i] == '0':
                    q.append(i)
                    if i == n - 1:
                        return True
            farthest = cur + maxJump
        return False