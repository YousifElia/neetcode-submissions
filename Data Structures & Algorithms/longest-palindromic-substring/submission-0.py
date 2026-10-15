class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
            
                

# a  b  a  b  d
#      l,r              # Save as a result
# a  b  a  b  d
#    l     r            # Save as a res
# a  b  a  b  d
# l           r         # exit out of loop and return res
# 
# a  b  b  c
#    l  r               # Save Result
# a  b  b  c
# l        r            Exit loop
# 
# a  c  d  d  c  a  j  i
#          l  r                 Does not work bc acddca is the longest substring but it will never find it because the string must be in the