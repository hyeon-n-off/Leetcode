class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        index, flag = 1, False

        for i in range(1, len(nums)):
            if (nums[i] == nums[i - 1]):
                if not flag:
                    nums[index] = nums[i]

                    index += 1
                    flag = True

            else:
                nums[index] = nums[i]
                
                index += 1
                flag = False
        
        return index