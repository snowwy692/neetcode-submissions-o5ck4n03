class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned =[c for c in s if c.isalnum()]

        cleaned="".join(cleaned).lower()

        return cleaned == cleaned[::-1]