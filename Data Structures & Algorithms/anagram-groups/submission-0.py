class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashm = defaultdict(list) #mapping char count of each str to list of anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1 # map ascii value to count

            hashm[tuple(count)].append(s) #append the string to this count pattern

        return list(hashm.values())
