class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            if str(sorted(word)) in groups:
                groups[str(sorted(word))].append(word)
            else:
                groups[str(sorted(word))] = [word]
        return groups.values()