class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)

        freq = [[] for i in range(len(nums)+ 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

