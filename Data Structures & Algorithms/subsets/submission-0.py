class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def sol(index):
            if index == len(nums):
                result.append(current.copy())
                return
            current.append(nums[index])
            sol(index+1)
            current.pop()
            sol(index+1)
        sol(0)
        return result 