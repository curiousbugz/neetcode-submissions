class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower="".join(c.lower() for c in s if c.isalnum())
        return True if lower==lower[::-1] else False
        