class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s.lower() if char.isalnum())
        for i in range(len(s)): 
            if s[i] != s[len(s)-i-1]: 
                return False
        
        return True

        