class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        mostFreq = (1,s[0])
        freqMap = {s[0]: 1}
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
                    if s[r] in freqMap:
                        freqMap[s[r]] += 1
                    else:
                        freqMap[s[r]] = 1
            
            for char,freq in freqMap.items():
                if freq > mostFreq[0]:
                    mostFreq = (freq, char)
            
        return max_window_size