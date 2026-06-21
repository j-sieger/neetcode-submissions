class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.getSumofSquares(n)
            if n == 1:
                return True
        return False
    
    def getSumofSquares(self, n:int) -> int:        
        temp = n
        happy = 0 
        while temp:
            digit = temp%10
            happy = happy + (digit**2)
            temp = temp//10
        return happy

        