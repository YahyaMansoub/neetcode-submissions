class Solution:
    def maxArea(self, heights: List[int]) -> int:


        l , r = 0, len(heights)-1
        max_water=0

        while l < r:

            w = r - l 
            h = min(heights[l],heights[r])
            area = h*w

            max_water = max(area, max_water)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return max_water



        