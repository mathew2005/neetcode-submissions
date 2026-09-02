class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set()
        l = 0
        r = 0
        maxLen = 0
        while r < len(s):
            # print(window,r)
            if s[r] in window:
                window.remove(s[l])
                l += 1
            else:
                window.add(s[r])
                r += 1
                maxLen = max(len(window), maxLen)

        return maxLen