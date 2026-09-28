class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {

        }
        for val in nums:
            if val not in hash_map:
                hash_map[val] = 1
            else:
                hash_map[val] +=1

        sorted_nums = sorted(hash_map, key=hash_map.get, reverse=True)
        return sorted_nums[:k]
