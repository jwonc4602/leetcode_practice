class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Given an array of integers nums which is sorted in ascending order,
        and an integer target, write a function to search target in nums. If
        target exists, then return its index. Otherwise, return -1.
        You must write an algorithm with O(log n) runtime complexity.
        """
        low, high = 0, len(nums) - 1
        while low <= high:  
            mid = (high + low) // 2  
            if target == nums[mid]: 
                return mid
            elif target > nums[mid]: 
                low = mid + 1
            else: 
                high = mid - 1
    
        return -1
