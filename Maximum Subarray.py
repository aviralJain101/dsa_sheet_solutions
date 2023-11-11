class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = max(nums)
        sum = 0
        for num in nums:
            sum += num
            max_sum = max(max_sum, sum)
            sum = max(sum, 0)
        return max_sum
        
