class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Hashmap/Heap? to store the letters in t
        count = {}

        for char in t:
            count[char] = count.get(char, 0) + 1

        window = {}
        left = 0
        right = 0
        satisfied = 0

        temp = ""
        minlength = float("inf")

        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in count and window[char] <= count[char]:
                satisfied += 1
            while satisfied == len(t):
                if right - left + 1 < minlength:
                    temp = s[left:right + 1]
                    minlength = right - left + 1
                char = s[left]

                if char in count and window[char] <= count[char]:
                    satisfied -= 1

                window[char] -= 1
                left += 1
            right += 1
        return temp


# create required hashmap
# create required window hashmap
# 
# left = 0
# right = 0
#  
# for i < s.length 
#   add s[right]
#   
#   if window is valid 
#       while window is still valid:
#           record window
#           remove s[left]
#           left++
#           
#   right++        
#           
#   return window

# Thought process
# Sliding Window
# Test Case: OUZODYXAZV
#
# ||OUZODYXAZV (sliding window to find the shortest substring
# O||UZODYXAZV (iterate til we find our first letter from our hashmap)
# OU||ZODYXAZV
# OU|Z|ODYXAZV (we find our first one so left pointer (hashmap fifills requirement) stays here while right continues to find the rest)
# OU|ZO|DYXAZV
# OU|ZOD|YXAZV
# OU|ZODY|XAZV (found Y, so we can subtract our counter from our hashmap -= 1)
# OU|ZODYX|AZV (found X, so we can subtract our counter from our hashmap -= 1)
# OU|ZODYXA|ZV
# OU|ZODYXAZ|V (we find that there is an extra Z, so we move left pointer to Y)
# OU|ZODYXAZV|
# OUZ|ODYXAZV|
# OUZO|DYXAZV|
# OUZOD|YXAZV|
# OUZOD|YXAZ|V
# edge case where we don't have an answer, we check if our hashmap are all 0, if not we return ""
