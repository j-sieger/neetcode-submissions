class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.getSumofSquares(n)
        while slow !=fast:
            fast = self.getSumofSquares(fast)
            fast = self.getSumofSquares(fast)
            slow = self.getSumofSquares(slow)
        return True if fast ==1 else False
        
    def getSumofSquares(self, n:int) -> int:        
        temp = n
        happy = 0 
        while temp:
            digit = temp%10
            happy = happy + (digit**2)
            temp = temp//10
        return happy        

######### Neetcode
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         visit = set()
#         while n not in visit:
#             visit.add(n)
#             n = self.getSumofSquares(n)
#             if n == 1:
#                 return True
#         return False
    
#     def getSumofSquares(self, n:int) -> int:        
#         temp = n
#         happy = 0 
#         while temp:
#             digit = temp%10
#             happy = happy + (digit**2)
#             temp = temp//10
#         return happy
####### My solutions #########
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         temp = n
#         happy = 0 
#         while temp:
#             digit = temp%10
#             happy = happy + (digit*digit)
#             temp = temp//10
#         if happy == 1:
#             return True
#         else:
#             try:
#                 return self.isHappy(happy)        
#             except:
#                 return False
        