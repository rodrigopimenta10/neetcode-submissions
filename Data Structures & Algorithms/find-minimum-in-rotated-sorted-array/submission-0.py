class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or not nums:
            return 0

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            #print(f'l:{l}, r:{r}, mid:{mid}')
        
        return nums[r]