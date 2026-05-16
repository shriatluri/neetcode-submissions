class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            max_area = max(area, max_area)
            # see if we can find taller on the left
            # we only skip lines that are shorter than or equal to the current shorter line
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_area