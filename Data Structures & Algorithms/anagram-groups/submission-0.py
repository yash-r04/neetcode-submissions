from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        dic = defaultdict(list)

        for i in range(len(strs)):
            arr = [0]*26
            for j in range(len(strs[i])):
                arr[ord(strs[i][j])-97]+=1

            dic.setdefault(tuple(arr),[]).append(strs[i])

        for key, value in dic.items():
            res.append(value)

        return res
        