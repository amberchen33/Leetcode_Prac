class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #print(bin(4), bin(14))
        x1 = bin(x)[2:]
        y1 = bin(y)[2:]
        num = 0
        large = max(len(x1), len (y1))
        # diff = abs(len(x1) - len (y1))
        # if len(x1)>len(y1):
        #    y1 = '0'*diff + y1
        # else:
        #    x1 = '0'*diff + x1
        
        y1 = '0' * (large - len(y1)) + y1
        x1 = '0' * (large - len(x1)) + x1  
        # for i in range(large):
        #     if x1[i] != y1[i]:
        #         num += 1
        #         print(num)
        for i, j in zip(x1, y1):
            if i != j:
                num += 1
        return num