class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = defaultdict(int)
        set_t = defaultdict(int)

        for char in s:
            set_s[char] += 1
        for char in t:
            set_t[char] += 1
        return set_s == set_t