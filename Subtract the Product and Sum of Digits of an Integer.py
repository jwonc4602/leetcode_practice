import numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        Given an integer number n, return the difference between the product of
        its digits and the sum of its digits.
        """
        x = [int(i) for i in str(n)]
        return numpy.prod(x) - sum(x)
      
# tried to use numpy, not that efficient

# Sample 14 ms submission
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        while n:
            ones = n % 10
            sum += ones
            product *= ones
            n //= 10
        return product - sum
