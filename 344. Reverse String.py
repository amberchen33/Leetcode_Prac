class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s)//2):
            print(i)
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            print(len(s)-1-i)
            s[len(s)-1-i] = tmp
        return ''.join(s)
        
        # a = s.split()
        # print(a)
        # a.reverse()
        # print(a)
        # return ''.join(a)
        #return s[::-1]
        