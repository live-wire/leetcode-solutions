import collections as c
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        dic = {}
        
        for i, size in enumerate(groupSizes):
            
            dic.setdefault(size, []).append(i)
           
            if len(dic[size]) == size:
                result.append(dic.pop(size))
        
        return result