class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {

        }
        
        for val in nums:
            if val in hash_map:
                return True
            else:
                hash_map[val] = True

        return False