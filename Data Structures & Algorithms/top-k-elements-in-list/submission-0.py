from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = {}
        for i in nums:
            if i in mem:
                mem[i] += 1
            else:
                mem[i] = 1
        
        # Sort by frequency in descending order and take first k
        return [key for key, _ in sorted(mem.items(), key=lambda x: x[1], reverse=True)[:k]]