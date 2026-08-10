class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: res += str(len(s)) + "*" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        while curr < len(s):
            length = ""
            while s[curr] != "*":
                length += s[curr]
                curr += 1
           
        
            res.append(s[curr + 1:curr + 1 + int(length)])
            curr += 1 + int(length)

        return res

