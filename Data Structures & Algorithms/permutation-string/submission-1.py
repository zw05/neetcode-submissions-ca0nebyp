class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        arr = [0] * 26
        for c in s1:
            arr[ord(c) - ord("a")] += 1 

        if n > m:
            return False
        
        l = 0
        r = 0 

        res = [0] * 26
        while r < m:
                res[ord(s2[r]) - ord("a")] += 1
                if res == arr:
                    return True
                elif r - l + 1 == n:
                        res[ord(s2[l]) - ord("a")] -= 1
                        l += 1
                r += 1
        return False



