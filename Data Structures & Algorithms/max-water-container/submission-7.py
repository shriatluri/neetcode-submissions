class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0

        while r > l:
            result = max(result, (r - l) * min(heights[l], heights[r]))
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return result

            