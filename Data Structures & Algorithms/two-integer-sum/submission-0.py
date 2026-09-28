class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map ={}

        
        for i,val in enumerate(nums):
            compliment = target - val
            if compliment in hash_map:
                return [hash_map[compliment],i]
            else:
                hash_map[val] = i