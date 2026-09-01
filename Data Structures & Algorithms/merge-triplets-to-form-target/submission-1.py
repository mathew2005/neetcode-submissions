class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = []
        res = set()
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]: continue
            good.append(triplet)
        
        for triplet in good:
            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    res.add(i)
        return len(res) == 3