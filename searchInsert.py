class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Given a sorted array of distinct integers and a target value,
        return the index if the target is found. If not, return the index
        where it would be if it were inserted in order.
        """
        low, up = 0, len(nums)
        while low < up:
            mid = (low + up) // 2
            if target <= nums[mid]:
                up = mid
            else:
                low = mid + 1
            
        return low 

