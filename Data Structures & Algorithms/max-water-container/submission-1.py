class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            container_size = ((right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
                if container_size > max_water:
                    max_water = container_size
            else:
                right -= 1
                if container_size > max_water:
                    max_water = container_size

        return max_water
