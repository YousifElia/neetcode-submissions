class Solution {
    public boolean hasDuplicate(int[] nums) {
        
    HashSet<Integer> sol = new HashSet<>();

    for (int num : nums) {
        if (sol.contains(num)) return true;
        sol.add(num);
    } return false;


        // for(; p1 < nums.length - 1; p1++) {
        //     for(int p2 = p1 + 1; p2 < nums.length; p2++) {
        //         if (nums[p1] == nums[p2]) {
        //             return true;
        //         } 
        //     } 
        // }
        // return false;
    }
}