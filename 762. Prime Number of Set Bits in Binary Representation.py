class Solution:
            
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def isprime(num):
            if num == 1:
                return 0
            elif num == 2:
                return 1
            elif num == 3:
                return 1
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return 0
            return 1      
        ans = []            
        for i in range(L, R+1):
            j = []
            j.append(bin(i)[2:])
            l = list(j[0])
            ans.append(isprime(l.count('1')))
        return sum(ans)