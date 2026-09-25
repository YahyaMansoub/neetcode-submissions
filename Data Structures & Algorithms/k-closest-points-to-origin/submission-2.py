class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = [
            (x*x + y*y, [x, y])
            for x, y in points
        ]

        heapq.heapify(pts)
        res = []
        for _ in  range(k):
            d, p=heapq.heappop(pts)
            res.append(p)
        return res