import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours(k):
            return sum(math.ceil(p / k) for p in piles)

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if get_hours(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left
