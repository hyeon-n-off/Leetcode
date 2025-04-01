class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n >= k:
            nums[:] = nums[-k:] + nums[:-k]
        else:
            r = (k - n) % n
            nums[:] = nums[-r:] + nums[:-r]