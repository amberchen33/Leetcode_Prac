class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n1 = bin(n)[2:]
        check = []
        for i in n1:
            ans = True
            if not check:
                check.append(i)
                print(check[-1])
            elif i != check[-1]:
                check.append(i)
            else:
                ans = False
                break
        return ans