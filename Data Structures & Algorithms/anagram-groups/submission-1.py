from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hwo to check if two strings are anagram
            # 1. sort them -> then check if they are teh same (O(nlogn + n))
            # 2. store in a set
        dictionary = defaultdict(list)
        for s in strs:
            s.lower()
            freq = [0] * 26
            for char in s:
                freq[ord(char) - 97] += 1
        
            dictionary[tuple(freq)].append(s)
        res = []
        for key,value in dictionary.items():
            res.append(value)

        return res