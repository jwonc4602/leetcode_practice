class Solution:
    def reverseWords(self, s: str) -> str:
        """Given a string s, reverse the order of characters in each word within
        a sentence while still preserving whitespace and initial word order.
        """
        x = s.split(" ")
        for i in range(len(x)):
            x[i] = x[i][::-1]
        return ' '.join(x)
