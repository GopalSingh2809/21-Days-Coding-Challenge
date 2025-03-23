class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        from collections import defaultdict

        if not s or not t or len(s) < len(t):
            return ""

        # Frequency map for characters in t
        t_freq = defaultdict(int)
        for char in t:
            t_freq[char] += 1

        # Variables for the sliding window
        left, right = 0, 0
        min_length = float('inf')
        start = 0
        count = len(t)

        # Expand the window
        while right < len(s):
            if s[right] in t_freq:
                if t_freq[s[right]] > 0:
                    count -= 1
                t_freq[s[right]] -= 1

            right += 1

            # Contract the window
            while count == 0:
                if right - left < min_length:
                    min_length = right - left
                    start = left

                if s[left] in t_freq:
                    t_freq[s[left]] += 1
                    if t_freq[s[left]] > 0:
                        count += 1

                left += 1

        return "" if min_length == float('inf') else s[start:start + min_length]
    
ans=Solution()
print(ans.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(ans.minWindow("a","a")) # "a"
print(ans.minWindow("a","aa")) # ""