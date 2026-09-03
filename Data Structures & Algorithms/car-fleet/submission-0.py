class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        pair.sort(reverse=True)
        for p,v in pair:
            t = (target - p)/v
            stack.append(t)
            if (len(stack) >= 2) and (stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)