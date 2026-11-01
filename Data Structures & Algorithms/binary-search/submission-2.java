class Solution {
    public int search(int[] nums, int target) {

        if(nums.length == 0) return -1;
        int left = 0, right = nums.length - 1, mid = nums.length / 2;

        while (left <= right) {
            if(nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
               left++;
            } else right--;
        } return -1;
    }
}