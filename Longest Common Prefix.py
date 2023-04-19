class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an
        array of strings. If there is no common prefix, return an empty string "".

        preconditions: 1 <= strs.length <= 200
        0 <= strs[i].length <= 200
        strs[i] consists of only lowercase English letters.
        >>> longestCommonPrefix(["flower","flow","flight"])
        "fl"
        >>> longestCommonPrefix(["dog","racecar","car"])
        ""
        """
        
        # when input is an empty list
        if not strs:
            return ''
   
        # find shortest len to avoid index error
        lens = [len(items) for items in strs]
        min_len = min(lens)
        result = ''
        
        for i in range(1, min_len+1):
            prefix = strs[0][:i]
            for s in strs:             
                if s[:i] != prefix:
                    return result
            result = prefix
            
        return result
