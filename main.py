class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        s=0
        if s in nums: return s
        nums.append(0)
        nums=sorted(nums)

        if s==max(nums):
           return (((nums[:nums.index(0)][-1])))
        elif s==min(nums):
            return ((nums[nums.index(0) + 1:][0]))
        elif (abs(((nums[nums.index(0) + 1:][0])))-0) >(abs(nums[:nums.index(0)][-1])-0):
            return ((nums[:nums.index(0)][-1]))
        else: return ((nums[nums.index(0) + 1:][0]))