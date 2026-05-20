class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for item in strs:
            ordered_str = "".join(sorted(item))
            if ordered_str in anagrams:
                anagrams[ordered_str].append(item)
            else:
                anagrams[ordered_str] = [item]
        return list(anagrams.values())