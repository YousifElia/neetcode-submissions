class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count frequencies
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Convert map entries to list and sort by value (frequency) descending
        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(freqMap.entrySet());
        entries.sort((a, b) -> b.getValue() - a.getValue());

        // Take first k keys
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = entries.get(i).getKey();
        }
        return result;
    }
}