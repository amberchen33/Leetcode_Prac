class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = set("qwertyuiop") 
        b = set("asdfghjkl")
        c = set("zxcvbnm")
        ans = []
        for i in words:
            #if len(a - si) == 0 差集
            si = set(i.lower())
            if si.issubset(a) or si.issubset(b) or si.issubset(c):
                ans.append(i)
                
        return ans