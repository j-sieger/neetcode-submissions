class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        happy = 0 
        while temp:
            digit = temp%10
            happy = happy + (digit*digit)
            temp = temp//10
        if happy == 1:
            return True
        else:
            try:
                return self.isHappy(happy)        
            except:
                return False

        