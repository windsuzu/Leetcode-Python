from collections import defaultdict, Counter

class Solution:
	# Using HashTable
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cs, ct = defaultdict(int), defaultdict(int)
        
        for i in range(len(s)):
            cs[s[i]] += 1
            ct[t[i]] += 1
        
        for k, v in cs.items():
            if ct[k] != v:
                return False
        return True
    
    
	# Using Counter
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
		
  
	# Using Sorted
    def isAnagram3(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)