from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        pairs = list(count.items())

        pairs.sort( key=lambda x: x[1], reverse=True)

        return [num for num, freq in pairs[:k]]


            

        

        

        