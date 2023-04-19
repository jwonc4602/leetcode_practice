class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Given two non-negative integers low and high. Return the count of odd
        numbers between low and high (inclusive).
        """
        count = 0
        total = (high - low) + 1
        
        if total % 2 == 0:
            count += (total // 2)
        else:
            if low % 2 != 0:
                count += (total // 2) + 1
            else:
                count += total // 2
        return count
