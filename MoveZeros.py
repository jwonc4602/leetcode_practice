class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Given an integer array nums, move all 0's to the end of it
        while maintaining the relative order of the non-zero elements.
        Do not return anything, modify nums in-place instead.
        """
        i = nums.count(0)
        while i > 0:
            nums.remove(0)
            nums.append(0)
            i -= 1
