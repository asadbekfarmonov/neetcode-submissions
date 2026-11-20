class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_substring = set()
        maxs = 0
        while right < len(s):
            while s[right] in max_substring:
                max_substring.remove(s[left])
                left += 1

            max_substring.add(s[right])
            maxs = max(maxs,right - left + 1)
            right += 1
        
        return maxs