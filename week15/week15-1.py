class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        N=len(nums)
        return nums[N-1]*nums[N-2]-nums[1]*nums[0]