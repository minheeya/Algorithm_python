from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        
        anagrams_dic = defaultdict(list)
        for str in strs:
            anagrams_dic[''.join(sorted(str))].append(str)
        
        return list(anagrams_dic.values())
    
#str = 'eat' 일 경우, sorted(str)하면 ['a', 'e', 't'] 반환
#str.sort()하면 AttributeError: 'unicode' object has no attribute 'sort'발생