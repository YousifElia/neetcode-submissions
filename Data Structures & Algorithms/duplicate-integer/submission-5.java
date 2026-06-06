class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        HashSet<Integer> sol = new HashSet<>();

        for(int num : nums) {
            sol.contains(num);
            if (!sol.add(num)) return true;
        }
        return false;
    }
}