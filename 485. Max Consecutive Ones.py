class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tem = 0
        result = 0
        for i in nums:
            if i == 1:
                tem += 1
                result = max(tem, result)
            else:
                tem = 0
        return result  