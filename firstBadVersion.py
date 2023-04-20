# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, up = 0, n-1
        while low <= up:
            mid = (low + up) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
            else:
                up = mid - 1
        return low
