class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []
        def sol(index,remaining):
            if remaining == 0:
                result.append(current.copy())
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    return
                current.append(candidates[i])
                sol(i+1,remaining-candidates[i])
                current.pop()
        sol(0,target)
        return result
