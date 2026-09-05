class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int result = 0, left = 0;

        for(int right = 0; right < s.length(); right++) {
            count[s.charAt(right) - 'A']++;

            int maxFreq = 0;
            for(int val : count)
                maxFreq = Math.max(maxFreq, val);
            
            while((right - left + 1) - maxFreq > k) {
                count[s.charAt(left) - 'A']--;
                left++;

                maxFreq = 0;
                for(int val : count) 
                    maxFreq = Math.max(maxFreq, val);
                
            }
            result = Math.max(result, right - left + 1);
        }
        return result;
    }
}
