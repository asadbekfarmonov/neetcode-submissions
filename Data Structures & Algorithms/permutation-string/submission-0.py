class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        permut = {}
        window = {}

        for i in s1:
            permut[i] = permut.get(i, 0) + 1
        
        while right < len(s2):
            window[s2[right]] = window.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            if window == permut:
                return True
            
            right += 1

        return False