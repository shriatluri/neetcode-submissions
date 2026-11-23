class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            heightL = heights[l]
            heightR = heights[r]

            vol = min(heightL, heightR) * (r - l)
            result = max(result, vol)

            if heightL < heightR:
                l += 1
            else:
                r -= 1
        
        return result



            