class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        res.append((nums[i],nums[j],nums[k]))
        s = set(res)
        res = []
        for tup in s:
            res.append(list(tup))
        return res