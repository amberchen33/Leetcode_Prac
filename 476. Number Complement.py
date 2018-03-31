class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # b = bin(num)[2:]
        # ans = 0
        # count = len(b)-1
        # com = []
        # for i in b:
        #     if i == '1':
        #         com.append('0')
        #     else: com.append('1')
        #     print(com)
        #com = ''.join('0' if n == '1' else '1' for n in bin(num)[2:])
        #format(num, 'b')
        #print(com)
        # for j in com:
        #     ans += (2**count)*int(j)
        #     count = count - 1
        bit = len(bin(num))-2
        return 2**bit-1-num
        #return int(com, 2)
        
        #x = ''.join('0' if n == '1' else '1' for n in bin(num)[2:])