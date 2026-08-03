public class Solution {
    public int maxArea(List<Integer> heights) {
        // Convert the List to a primitive array for fast indexing
        int n = heights.size();
        int[] h = new int[n];
        for (int i = 0; i < n; i++) {
            h[i] = heights.get(i);
        }
        return maxArea(h);               // delegate to the array version
    }

    // ----- New overload that works directly with an int[] -----
    public int maxArea(int[] heights) {
        int left = 0, right = heights.length - 1, best = 0;

        while (left < right) {
            int height = Math.min(heights[left], heights[right]);
            int width = right - left;
            best = Math.max(best, height * width);

            // Move the pointer at the shorter line inward
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return best;
    }
}
