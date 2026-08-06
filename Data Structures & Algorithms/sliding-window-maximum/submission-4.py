class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = k-1
        highestindex = None
        answers = []
        while True:
            if not highestindex or highestindex < start:
                highestindex = start
                for i in range(start,end+1):
                    if nums[i]>nums[highestindex]:
                        highestindex = i
            else:
                if nums[highestindex] < nums[end]:
                        highestindex = end
            answers.append(nums[highestindex])
            start+=1
            end+=1
            if end == len(nums):
                break
        return answers
                    