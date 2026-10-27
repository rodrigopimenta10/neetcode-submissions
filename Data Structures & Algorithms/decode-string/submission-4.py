from collections import Counter
class Solution:
    def decodeString(self, s: str) -> str:

        def dfs(cur):
            counter = Counter()
            print(cur)
            if len(cur) == 1 or len(cur) == 0:
                return cur
            elif cur[0].isdigit():
                cur_int = cur[0]
                i = 1
                while cur[i].isdigit():
                    cur_int += cur[i]
                    i += 1
                counter['['] = 1
                i, start = i+1, i+1
                while counter['['] - counter[']'] != 0:
                    if cur[i] == '[': counter['['] += 1
                    elif cur[i] == ']': counter[']'] += 1
                    i += 1
                print(cur_int, i)
                return int(cur_int) * dfs(cur[start:i-1]) + dfs(cur[i:]) 

            else: #Is char
                return cur[0] + dfs(cur[1:])


        return dfs(s)