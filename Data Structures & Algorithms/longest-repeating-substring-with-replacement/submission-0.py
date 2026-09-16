class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        freqMap, freqChar = {s[0]: 1}, [s[0], 1]
        max_window_size = 1
        while r < len(s):
            if s[r] in freqMap: 
                freqMap[s[r]] += 1
            else: 
                freqMap[s[r]] = 1
            window_size = r - l + 1

            for char,freq in freqMap.items():
                if freq > freqChar[1]:
                    freqChar = [char, freq]

            if k < window_size - freqChar[1]:
                # print("ran out of replacements")
                freqMap[s[l]] -= 1
                l += 1
            else:
                max_window_size = max(window_size, max_window_size)
            r += 1
            
        return max_window_size
            