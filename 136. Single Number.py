class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans   