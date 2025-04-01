class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index, check = 1, nums[0]

        for i in range(1, len(nums)):
            if nums[i] != check:
                nums[index] = nums[i]
                index, check = index + 1, nums[i]

        return index