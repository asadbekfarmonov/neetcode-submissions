class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map = {

        }

        for val in s:
            if val not in hash_map:
                hash_map[val] = 1
            else:
                hash_map[val] +=1
        
        for val in t:
            if val in hash_map:
                hash_map[val] -=1
                if hash_map[val] < 0:
                    return False
            else:
                return False

        return True