class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n+1):
            print(i)
            if i%3 == 0 and i%5 == 0: 
                i = "FizzBuzz"
            elif i%3==0:
                i = "Fizz"
            elif i%5==0:
                i = "Buzz"
            ans.append(str(i))
        return ans