class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        #print([S.count(j) for j in J])
        
        print([s in J for s in S])
        return sum(S.count(j) for j in J)  
            