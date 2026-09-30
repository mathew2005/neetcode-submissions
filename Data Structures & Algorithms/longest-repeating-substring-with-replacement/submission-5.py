class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqMap = {}
        mostFreq = 1
        max_window_size = 1
        for r in range(len(s)):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            mostFreq = max(mostFreq, freqMap[s[r]])

            while (r-l) + 1 - mostFreq > k:
                freqMap[s[l]] -= 1
                l += 1
            max_window_size  = max(max_window_size, (r-l) + 1)
            
        return max_window_size