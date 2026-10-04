class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = ""
        bit, count = 0, 0
        while n >= 1:
            bit = n % 2
            bits += str(bit)
            n = n // 2
        for char in bits:
            if char == "1":
                count += 1
        return count

# n = 5
# 5 mod 2 = 1
# bits += str(1) so bits = "1"
# 5 // 2 = 2 
# 
# 2 mod 2 = 0
# bits += str(0) so bits = "10"
# 2 // 2
# 
# 1 mod 2 = 1
# bits += str(1) so bits = "101"
# 1 // 2
# 
# then we have a for loop for char == "1" where it loops through bits
# and if there is a one it adds to the counter
