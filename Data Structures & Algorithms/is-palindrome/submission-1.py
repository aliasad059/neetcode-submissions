class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s.lower() if char.isalnum())
        n=len(s)
        for i in range(n): 
            if s[i] != s[n-i-1]: 
                return False
        
        return True

        