from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        s = sorted(hand)
        counter_dict = Counter(s)
        print(s)
        print(counter_dict)
        print()

        while counter_dict: 
            sorted_keys = sorted(counter_dict.keys())
            prev = sorted_keys[0]
            cur_lst = [prev]
            counter_dict[prev] -= 1
            if counter_dict[prev] == 0:
                del counter_dict[prev]
            print(sorted_keys,prev)
            for i in range(0,groupSize):
                #print(f'{cur_lst},{i}')
                if len(sorted_keys) < groupSize:
                    return False
                elif sorted_keys[i] == prev:
                    continue
                    #i += 1
                elif sorted_keys[i] != (prev+1):
                    print(sorted_keys[i], (prev+1))
                    return False
                else:  # s[i] == prev+1
                    
                    counter_dict[sorted_keys[i]] -= 1
                    if counter_dict[sorted_keys[i]] == 0:
                        del counter_dict[sorted_keys[i]]
                    cur_lst.append(sorted_keys[i])
                    prev = sorted_keys[i]
                    #counter += 1
                    print(f'{cur_lst},{counter_dict}')
                    #i += 1
            print(f'{cur_lst}')
            print()
        if len(counter_dict) == 0:  # If it is empty
            return True
        return False


            