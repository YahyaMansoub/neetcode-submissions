class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        candidates.sort()
        res = []


        def bt(idx , p , s):
            if s == target:
                res.append(p[:])
                return 
            if s > target:
                return 
            
            for i in range(idx, len(candidates)):

                if i > idx and candidates[i] == candidates[i-1]:
                    continue 
                if s+candidates[i] > target:
                    break
                p.append(candidates[i])
                bt(i+1, p, s+candidates[i])
                p.pop()
            
        bt(0, [], 0)
        return  res
        