class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # Iterate through the characters of the first string
        for i, char in enumerate(strs[0]):
        # Compare the character with the corresponding characters in the other strings
            for j in range(1, len(strs)):
            # If the characters don't match, return the common prefix found so far
                if i >= len(strs[j]) or char != strs[j][i]:
                    return strs[0][:i]

        # Return the whole first string if it is the common prefix
        return strs[0]
