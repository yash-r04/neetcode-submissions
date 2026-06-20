class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        l = []
        for i in range(len(digits)):
            num += digits[-(i+1)]*(10**i)

        num +=1
        nums = num

        for i in range(len(digits)+1):
            num = nums% 10
            nums = nums//10
            l.insert(0, num)
            
        if l[0] == 0:
            l.pop(0)
        return (l)

