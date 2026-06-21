class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = [char for char in s if char.isalnum()]
        # cleaned_s = ''.join(cleaned_s)
        n = len(cleaned_s)        
        for i in range(n//2):
            if cleaned_s[i].lower() != cleaned_s[n-i-1].lower():                
                return False
            
        return True
