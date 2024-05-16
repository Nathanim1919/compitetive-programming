class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        char_index = {}

        for end in range(len(s)):
            if s[end] in char_index and start <= char_index[s[end]]:
                start = char_index[s[end]] + 1
            else:
                maxLength = max(maxLength, end - start + 1)

            char_index[s[end]] = end

        return maxLength
