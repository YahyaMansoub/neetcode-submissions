class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0


        l, r = 0, len(heights)-1


        while l<r:
            ans = max(ans, min(heights[r], heights[l])*(r-l))

            if heights[r]>heights[l]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1

            else:
                l+=1
                r-=1

        return ans

        



        