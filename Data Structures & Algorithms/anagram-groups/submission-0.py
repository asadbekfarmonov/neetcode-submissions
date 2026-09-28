class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {

        }

        for val in strs:
            #sorted() comes as list
            #lists are unhashable
            #revert to str
            sorted_str = ''.join(sorted(val))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [val]
            else:
                hash_map[sorted_str].append(val)

        return list(hash_map.values())