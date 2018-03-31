class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left, right+1):
            x = i
            while x:
                x, j = x // 10, x % 10
                print('x, j => %s, %s' % (x, j))