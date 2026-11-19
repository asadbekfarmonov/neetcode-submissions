class Solution:
    def trap(self, height: List[int]) -> int:
        # water = 0
        # for i in range(len(height)):
        #     max_left = max(height[:i+1])
        #     max_right = max(height[i:])
            
        #     water += min(max_left, max_right) - height[i]

        # return water

        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        #prefix
        max_l = 0
        for i in range(len(height)):
            max_l = max(max_l, height[i])
            max_left[i] = max_l

        #suffix
        max_r = 0
        for i in range(len(height) - 1, -1 , -1):
            max_r = max(max_r, height[i])
            max_right[i] = max_r
        
        water = 0
        for i in range(len(height)):
            water += min(max_right[i], max_left[i]) - height[i]

        return water

