class Solution {
    public boolean hasDuplicate(int[] nums) {
        int p1 = 0;

        // HashSet<String> nums = new HashSet<>();

        for(; p1 < nums.length - 1; p1++) {
            for(int p2 = p1 + 1; p2 < nums.length; p2++) {
                if (nums[p1] == nums[p2]) {
                    return true;
                } 
            } 
        }
        return false;
    }
}