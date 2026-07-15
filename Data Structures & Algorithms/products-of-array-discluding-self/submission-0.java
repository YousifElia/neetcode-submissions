class Solution {
    public int[] productExceptSelf(int[] nums) {
    int totalProduct = 1, zeroCount = 0;

    // Count zeros and product of non-zero elements
    for (int num : nums) {
        if (num == 0) zeroCount++;
        else totalProduct *= num;
    }

    int[] ans = new int[nums.length];
    for (int i = 0; i < nums.length; i++) {
        if (zeroCount >= 2) {
            ans[i] = 0;
        } else if (zeroCount == 1) {
            ans[i] = (nums[i] == 0) ? totalProduct : 0;
        } else { // zeroCount == 0
            ans[i] = totalProduct / nums[i];
        }
    }
    return ans;
    }
}  
