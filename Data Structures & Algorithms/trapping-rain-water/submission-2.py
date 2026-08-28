class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        leftMax, rightMax = height[0], height[-1]
        while l < r: 
            if leftMax >= rightMax:
                r -= 1
                res += max(0, rightMax - height[r])
                rightMax = max(rightMax,height[r])
            else:
                l += 1
                res += max(0, leftMax - height[l])
                leftMax = max(leftMax,height[l])
        
        return res