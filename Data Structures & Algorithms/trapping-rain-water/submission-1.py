class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax, res = [], [], 0
        currLeft, currRight = 0, 0
        for h in height: currLeft = max(currLeft, h); leftMax.append(currLeft)
        for i in range(len(height) - 1, -1, -1): currRight = max(currRight,height[i]); rightMax.append(currRight)
        for i in range(1, len(height) - 1):
            res += max(0,min(leftMax[i-1], rightMax[len(height) - i - 1]) - height[i])
        return res

