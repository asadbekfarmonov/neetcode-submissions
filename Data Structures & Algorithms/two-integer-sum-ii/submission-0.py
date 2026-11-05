class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen() = 0
        # for i in numbers:
        #     seen.add(i)
        
        # res = [0,0]
        # for i, val in enumerate(numbers):
        #     rem = target - val
        #     if rem in seen():
        #         res = [i, seen(rem)]
        #         return res
        
        # return res

        # hash_map ={}

        
        # for i,val in enumerate(numbers):
        #     compliment = target - val
        #     if compliment in hash_map:
        #         return [hash_map[compliment] + 1,i + 1]
        #     else:
        #         hash_map[val] = i



        # left = 0
        # right = len(numbers) - 1
        # res = [0,0]
        # while left < right:
        #     if numbers[left] + numbers[right] > target:
        #         right -= 1
        #         continue
        #     elif numbers[left] + numbers[right] < target:
        #         left += 1
        #         continue
        #     else:
        #         res = [left + 1, right + 1]
        #         return res

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]
            