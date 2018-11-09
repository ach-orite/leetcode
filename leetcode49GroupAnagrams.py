from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = defaultdict(list)
        for s in strs:
            hash_map[''.join(sorted(s))].append(s)
        return [value for _, value in hash_map.items()]



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
sl = Solution()
print(sl.groupAnagrams(strs))