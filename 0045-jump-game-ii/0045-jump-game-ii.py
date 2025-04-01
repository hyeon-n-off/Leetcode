class Solution:
    def jump(self, nums: list[int]) -> int:
        max_reachable = 0
        index, count = 0, 0

        if len(nums) == 1:
            return 0

        for i, jump in enumerate(nums):

            if i + jump > max_reachable:
                max_reachable = i + jump
                 
            if i >= index:
                count += 1
                index = max_reachable
            
            if index >= len(nums) - 1:
                return count
