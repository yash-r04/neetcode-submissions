class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []

        dic ={}

        for i in nums:
            dic[i] = 1 + dic.get(i,0)

        dic = sorted(dic, key=dic.get, reverse = True)

        for i in range(k):
            res.append(dic[i])

        return res
        