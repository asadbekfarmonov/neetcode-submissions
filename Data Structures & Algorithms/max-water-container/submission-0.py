class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxsum = 0

        while left < right:
            current_sum = min(heights[left], heights[right]) * (right - left)
            maxsum = max(maxsum,current_sum)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxsum