class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        def sol(current,index):
            if sum(current) > target:
                return
            if sum(current) == target:
                result.append(current.copy())
                return
            for i in range(index,len(nums)):
                current.append(nums[i])
                sol(current,i)
                current.pop()
        sol([],0)
        return result

