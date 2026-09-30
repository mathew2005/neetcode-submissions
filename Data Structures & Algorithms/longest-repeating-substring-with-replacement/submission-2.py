class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        freqMap, mostFreq = {s[0]: 1}, (1,s[0])
        max_window_size = 0
        while r < len(s):
            window_size = (r - l + 1)
            changes = window_size - mostFreq[0]

            if changes > k: 
                freqMap[s[l]] -= 1    
                l += 1
            else:
                max_window_size = max(window_size, max_window_size)
                r += 1
                if r < len(s):
                    freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            
            for char,freq in freqMap.items():
                if freq > mostFreq[0]: mostFreq = (freq, char)
            
        return max_window_size