class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()


        def bt(idx, curr, s):

            if s == 0:
                res.append(curr[:])
                return 

            elif s < 0:
                return 

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i]==candidates[i-1]:
                    continue 
                curr.append(candidates[i])
                bt(i+1, curr, s- candidates[i])
                
                curr.pop()
        bt(0, [], target)
        return res

        