class Solution {
    public boolean hasDuplicate(int[] nums) {
        int p1 = 0;
        int p2 = 1;

        // HashSet<String> nums = new HashSet<>();

        for(; p1 < nums.length; p1++) {
            if (p1 == p2) {
                return true;
            }
            for(; p1 < nums.length; p1++) {
                if (p1 == p2) {
                    return true;
                } 
            } 
            p1 += 1;
            p2 += 1;
        } else {
            return false;
        }
    }
}