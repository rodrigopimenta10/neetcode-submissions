class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
            
        cur_gas, start = 0, 0
        # if gas[0] >= cost[0]:
        #     cur_gas = gas[0]-cost[0]
        # else:
        #     start += 1
        #     cur_gas = 0
        for i in range(0,len(gas)):
            print(f'gas:{cur_gas}, i:{i}, start:{start}')
            cur_gas += gas[i]
            if cur_gas >= cost[i]:
                cur_gas = cur_gas - cost[i]
            else:
                start = i+1
                cur_gas = 0 
            
        return start