class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        
        curr = n
        counter = 0
        while curr != 0:
            rem = curr % 2
            curr = curr // 2


            if rem == 1:
                counter += 1

            if curr == 1:
                counter += 1
                break

        return counter