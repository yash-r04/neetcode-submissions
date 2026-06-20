class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag =0
        sume =0
        if len(s)!= len(t):
            return False
        return sorted(s)==sorted(t)

            
            

        