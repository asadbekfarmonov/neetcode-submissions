class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # left = 0
        # right = len(numbers) - 1

        # while left < right:
        #     rem = numbers[left] + numbers[right]

        #     if total > target:
        #         right -= 1
        #     elif total < target:
        #         left += 1
        #     else:
        #         return [left + 1, right + 1]
        # nums.sort()
        # left = 0
        # right = len(numbers) - 1

        # while left < right:
        #     rem = numbers[left] + numbers[right]

        #     if total > target:
        #         right -= 1
        #     elif total < target:
        #         left += 1
        #     else:
        #         return [left + 1, right + 1]


        nums.sort()
        res = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res
