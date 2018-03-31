class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums => [3,2,4]
        
        for index1, num1 in enumerate(nums):
            num2 = target - num1
            if num1 == num2 and nums.count(num1) == 2:
                nums.remove(num1)
                index2 = nums.index(num2) + 1
                return index1, index2
            if num1 != num2 and num2 in nums:
                index2 = nums.index(num2)
                return index1, index2
            