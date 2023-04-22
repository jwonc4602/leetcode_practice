class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Given an integer array nums, rotate the array
        to the right by k steps, where k is non-negative.
        Do not return anything, modify nums in-place instead.
        """
        while k != 0:
            nums.insert(0, nums.pop())
            k -= 1
            

# other possible solution with less runtime
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        nums[:n-k]=nums[:n-k][::-1]
        nums[n-k:]=nums[n-k:][::-1]
        nums[:]=nums[::-1]
