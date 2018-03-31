class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = []
        for i in ops:
            if i == 'D':
                ans.append(ans[-1]*2)
            elif i == 'C':
                ans.pop()
            elif i == '+':
                ans.append(ans[-1]+ans[-2])
            else:
                ans.append(int(i))       
        return sum(ans) 