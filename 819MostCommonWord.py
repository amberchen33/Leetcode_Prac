from string import punctuation

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        dic = {}
        par = paragraph.split(" ")
        #print(par)
        for p in par:
            p = p.lower()
            #remove punctuation before adding into dic
            p = ''.join(c for c in p if c not in punctuation)
            if p not in dic.keys():
                dic[p] = 1
            else:
                dic[p] += 1
        print(dic)
        for b in banned:
            if b in dic.keys():
                del dic[b]
        return max(dic, key=dic.get)