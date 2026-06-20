class Solution:
    def isPalindrome(self, s: str) -> bool:
        strr = ''
        for i in s:
            if i.isalnum():
                strr += i.lower()

        return strr == strr [::-1]

            
        