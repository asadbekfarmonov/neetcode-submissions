class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        current = 0
        count = 1
        max_count = 1

        while current < len(nums) - 1:
            if nums[current] + 1 == nums[current + 1]:
                count += 1
            elif nums[current] == nums[current + 1]:
                pass
            else:
                count = 1

            max_count = max(max_count, count)
            current += 1

        return max_count